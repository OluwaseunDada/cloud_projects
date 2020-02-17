

from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.group.readonly',
    'https://www.googleapis.com/auth/admin.directory.user.readonly',
    'https://www.googleapis.com/auth/admin.directory.group.member.readonly',
]

SERVICE_ACCOUNT_FILE = "the-service-account.json"
DELEGATED_ACCOUNT='email_address_of_person_delegating_permission'
DOMAIN = 'xxxx.extension' # domain e.g. website_name.com

USERS = [
    #"firstname1.lastname1@somedomain.extension"
    "firstname2.lastname2@somedomain.extension"
    #"firstname3.lastname3@somedomain.extension"
]


def main():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_creds = creds.with_subject(DELEGATED_ACCOUNT)
    service = build('admin', 'directory_v1', credentials=delegated_creds)

    for user in USERS:
        print(f"for user: {user}")

        response = service.groups().list(
        domain=DOMAIN,
        userKey=user).execute()
        groups = response.get('groups', [])
        for group in groups:
             print(group['name'])

    print("---")



if __name__ == '__main__':
    main()

