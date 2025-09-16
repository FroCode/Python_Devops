import boto3

def list_accounts():
    org = boto3.client("organizations")
    paginator = org.get_paginator("list_accounts")

    print("📋 Accounts in your AWS Organization:\n")
    for page in paginator.paginate():
        for acct in page["Accounts"]:
            print(f"- Name: {acct['Name']}, "
                  f"Id: {acct['Id']}, "
                  f"Email: {acct['Email']}, "
                  f"Status: {acct['Status']}")

if __name__ == "__main__":
    list_accounts()
