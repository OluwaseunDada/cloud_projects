


from googleapiclient.discovery import build
from google.oauth2 import service_account
SCOPES = [ 'https://www.googleapis.com/auth/admin.directory.group.readonly'
          ,'https://www.googleapis.com/auth/admin.directory.user.readonly'
          ,'https://www.googleapis.com/auth/admin.directory.group.member.readonly']

SERVICE_ACCOUNT_FILE = "the-service-account.json"
DELEGATED_ACCOUNT='email_address_of_person_delegating_permission'


def main():
  creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
  delegated_creds = creds.with_subject(DELEGATED_ACCOUNT)
  service = build('admin', 'directory_v1', credentials=delegated_creds)

  results = service.users().list(customer='my_customer', maxResults=500, orderBy='email').execute()
  users = results.get('users', [])

  if not users:
      print('No users in the domain.')
  else:
      print('Users:')
      for user in users:
          print(u'{0} ({1})'.format(user['primaryEmail'],
                                    user['name']['fullName']))


if __name__ == '__main__':
  main()
