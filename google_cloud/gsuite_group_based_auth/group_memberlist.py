

from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.group.member.readonly',
]

SERVICE_ACCOUNT_FILE = "the-service-account.json" #specify the location of the service account file

GROUP = "something@xxxx.extension" # the group email address


def main():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_creds = creds.with_subject('email_address_of_person_delegating_permission')
    service = build('admin', 'directory_v1', credentials=delegated_creds)

    print("---")
    print("All group members of: " + GROUP)

    allmembers = service.members().list(groupKey=GROUP).execute()
    for m in allmembers['members']:
        user = m['email']

        # service accounts are excluded
        if "gserviceaccount" in user:
            continue

        status = m['status']
        print("User: " + user + "\nStatus: " + status)
        print()

        if status == 'ACTIVE':
            pass


if __name__ == '__main__':
    main()

