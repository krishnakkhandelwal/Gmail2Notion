import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email import message_from_bytes

# Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def gmail_authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Refresh or log in if needed
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())
    return creds

def get_email_header(headers, name):
    for header in headers:
        if header['name'].lower() == name.lower():
            return header['value']
    return None

def get_email_body(payload):
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                text = base64.urlsafe_b64decode(data).decode('utf-8')
                return text
            elif part['mimeType'] == 'text/html':
                # Optional: you can parse HTML if preferred
                continue
    else:
        data = payload.get('body', {}).get('data')
        if data:
            text = base64.urlsafe_b64decode(data).decode('utf-8')
            return text
    return ""

def main():
    creds = gmail_authenticate()
    service = build('gmail', 'v1', credentials=creds)

    # Fetch the list of messages (max 20)
    result = service.users().messages().list(userId='me', maxResults=20).execute()
    messages = result.get('messages', [])

    if not messages:
        print("No messages found.")
        return

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = msg_data['payload']['headers']

        subject = get_email_header(headers, 'Subject')
        sender = get_email_header(headers, 'From')
        date = get_email_header(headers, 'Date')
        snippet = msg_data.get('snippet')

        body = get_email_body(msg_data['payload'])

        print(f"---\nSubject: {subject}\nFrom: {sender}\nDate: {date}\nSnippet: {snippet}\nBody:\n{body}\n")

if __name__ == '__main__':
    main()

