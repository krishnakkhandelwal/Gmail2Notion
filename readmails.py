# Make sure you have run:
# pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying scopes, delete token.json and re-run script for new consent
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def gmail_authenticate():
    creds = None
    # token.json stores user access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no valid credentials, let user login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            # Use fixed port 8080 to avoid callback issues
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())
    return creds

def get_message(service, user_id, msg_id):
    return service.users().messages().get(userId=user_id, id=msg_id, format='metadata').execute()

def main():
    creds = gmail_authenticate()
    service = build('gmail', 'v1', credentials=creds)

    # Fetch the latest 10 messages metadata
    results = service.users().messages().list(userId='me', maxResults=10).execute()

    messages = results.get('messages', [])
    if not messages:
        print("No messages found.")
        return

    for msg in messages:
        msg_data = get_message(service, 'me', msg['id'])
        print(f"Message ID: {msg['id']}, Snippet (metadata): {msg_data.get('snippet', '')}")

if __name__ == '__main__':
    main()
