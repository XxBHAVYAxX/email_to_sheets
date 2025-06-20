import os.path
import base64
import re
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/spreadsheets'
]

SPREADSHEET_ID = '1YklurCt1OHTVP7GGe8nJiLWUrfIXpav43ftK3UT9l6w'
RANGE_NAME = 'Sheet1!A:E'

def authenticate_google_apis():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def get_email_body(msg_payload):
    body_text = ""
    if 'parts' in msg_payload:
        for part in msg_payload['parts']:
            if part['mimeType'] == 'text/plain':
                if 'data' in part['body']:
                    body_text = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                    break
            elif part['mimeType'] == 'text/html':
                if not body_text and 'data' in part['body']:
                    body_text = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
            elif 'parts' in part:
                nested_body = get_email_body(part)
                if nested_body:
                    body_text = nested_body
                    break
    elif 'body' in msg_payload and 'data' in msg_payload['body']:
        body_text = base64.urlsafe_b64decode(msg_payload['body']['data']).decode('utf-8')
    body_text = re.sub(r'\s+', ' ', body_text).strip()
    return body_text[:200] + "..." if len(body_text) > 200 else body_text

def main():
    creds = authenticate_google_apis()
    try:
        gmail_service = build('gmail', 'v1', credentials=creds)
        sheets_service = build('sheets', 'v4', credentials=creds)
        print("Fetching emails from Gmail...")
        results = gmail_service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
        messages = results.get('messages', [])
        if not messages:
            print("No new messages found in inbox.")
            return
        emails_data = []
        emails_data.append(['Date', 'From', 'Subject', 'Body Snippet', 'Message ID'])
        for message in messages:
            msg = gmail_service.users().messages().get(userId='me', id=message['id'], format='full').execute()
            payload = msg['payload']
            headers = payload['headers']
            subject = ""
            sender = ""
            date = ""
            for header in headers:
                if header['name'] == 'Subject':
                    subject = header['value']
                elif header['name'] == 'From':
                    sender = header['value']
                elif header['name'] == 'Date':
                    date = header['value']
                    try:
                        date_obj = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z')
                        date = date_obj.strftime('%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        pass
            body_snippet = get_email_body(payload)
            message_id = msg['id']
            emails_data.append([date, sender, subject, body_snippet, message_id])
        print(f"Extracted {len(emails_data) - 1} emails. Updating Google Sheet...")
        body = {'values': emails_data}
        result = sheets_service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
            valueInputOption='RAW', body=body).execute()
        print(f"Cells appended: {result.get('updates').get('updatedCells')}")
        print("Script finished successfully!")
    except HttpError as error:
        print(f"An API error occurred: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
