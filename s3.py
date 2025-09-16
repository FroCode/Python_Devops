import boto3

# Initialize Organizations client
org = boto3.client("organizations")

# List of root emails for the accounts you want to invite
emails = [
    "inovaskd@inovaskdevelopment.dz",
    "maamar.haddouche@inovaskdevelopment.dz",
    "dhiya.kellouche@inovaskdevelopment.dz",
    "sabrine.benaboura@inovaskdevelopment.dz",
    "rihab.arioui@inovaskdevelopment.dz",
    "anes.ezziane@inovaskdevelopment.dz",
    "abdessamed.zetroni@inovaskdevelopment.dz",
    "lyna.ouabel@inovaskdevelopment.dz",
    "yousra.latreche@inovaskdevelopment.dz"
]

def send_invitation(email):
    try:
        response = org.invite_account_to_organization(
            Target={"Type": "EMAIL", "Id": email},
            Notes="Invitation to join the InovAsk AWS Organization."
        )
        handshake_id = response["Handshake"]["Id"]
        print(f"✅ Invitation sent to {email} (HandshakeId: {handshake_id})")
    except org.exceptions.DuplicateHandshakeException:
        print(f"⚠️ Invitation already sent to {email}")
    except Exception as e:
        print(f"❌ Failed to send invitation to {email}: {e}")

def main():
    for email in emails:
        send_invitation(email)

if __name__ == "__main__":
    main()
