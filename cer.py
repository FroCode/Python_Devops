import boto3
import csv
import time

org = boto3.client("organizations")
CSV_FILE = "users.csv"

def create_account(name, email):
    print(f"📦 Creating AWS account for {name} ({email})...")
    response = org.create_account(
        Email=email,
        AccountName=name,
        IamUserAccessToBilling="ALLOW"  # Allow IAM users/roles to access billing
    )
    create_id = response["CreateAccountStatus"]["Id"]

    # Wait until the account creation completes
    while True:
        status = org.describe_create_account_status(CreateAccountRequestId=create_id)
        state = status["CreateAccountStatus"]["State"]

        if state in ("SUCCEEDED", "FAILED"):
            return status["CreateAccountStatus"]
        print(f"⏳ Still creating {name}... current state: {state}")
        time.sleep(20)

def main():
    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            full_name = f"{row['Name']} {row['Surname']}"
            prof_email = row["Professional Email (https://webmail.inovaskdevelopment.dz/)"]

            result = create_account(full_name, prof_email)
            if result["State"] == "SUCCEEDED":
                print(f"✅ Account for {full_name} created. AccountId: {result['AccountId']}")
            else:
                print(f"❌ Failed to create account for {full_name}: {result.get('FailureReason')}")

if __name__ == "__main__":
    main()
