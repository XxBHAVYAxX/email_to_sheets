📧 Email to Google Sheets
A Python script that reads the latest emails from your Gmail inbox and writes their details (Date, Sender, Subject, Snippet, Message ID) into a Google Sheet automatically.

🔧 Features
Fetches the 10 most recent emails from Gmail.

Extracts and cleans the body snippet (supports plain text and HTML).

Stores email metadata in a Google Sheet:

Date

Sender

Subject

Body Snippet

Message ID

Handles authentication with Gmail and Sheets API via OAuth 2.0.

📂 Project Structure
bash
Copy
Edit
email_to_sheets/
├── email_to_sheet.py          # Main script
├── credentials.json           # OAuth2 credentials from Google Cloud
└── token.json                 # Auto-generated token after authentication
🔌 Requirements
Python 3.6+

Google APIs:

Gmail API (read-only)

Google Sheets API

Python Dependencies
Install dependencies using pip:

bash
Copy
Edit
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
📝 Setup Instructions
Enable APIs:

Go to the Google Cloud Console.

Create a project and enable:

Gmail API

Google Sheets API

Download Credentials:

Navigate to "OAuth 2.0 Client IDs"

Download the credentials.json file and place it in your project root.

Set Spreadsheet Access:

Share your Google Sheet with the email address listed in your token.json (after first run).

Update the SPREADSHEET_ID in the script to match your target Sheet.

Run the Script:

bash
Copy
Edit
python email_to_sheet.py
You will be prompted to authorize access on the first run.

📌 Notes
Only the 10 most recent emails from the inbox are fetched.

The body snippet is trimmed to 200 characters for readability.

Repeated executions will append data to the sheet.

📸 Sample Output (in Google Sheets)
Date & Time	From	Subject	Body Snippet	Message ID
2025-06-19 12:45:00	test@example.com	Welcome!	Thank you for signing...	17c2abc123d

📄 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Made with 💻 by Bhavya Kanojia
