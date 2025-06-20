# 📧 Email to Google Sheets

This is a simple Python script that reads your 10 most recent Gmail messages and pushes the key details into a Google Sheet. It's useful for automating data entry or tracking email interactions.

---

## ✨ Features

- Authenticates with Gmail and Google Sheets using OAuth 2.0.
- Fetches the latest 10 emails from your Gmail inbox.
- Extracts the following information:
  - 📅 Date
  - 📤 From
  - 📝 Subject
  - 📄 Body snippet (cleaned and trimmed)
  - 🆔 Gmail Message ID
- Appends the data into a Google Sheet (Sheet1!A:E).

---

## 📦 Requirements

- Python 3.6 or higher
- Gmail API enabled
- Google Sheets API enabled

### 📚 Install dependencies

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
---

## ⚙️ Setup Instructions

1. **Google Cloud Setup:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project.
   - Enable the following APIs:
     - Gmail API
     - Google Sheets API

2. **OAuth Credentials:**
   - In the same project, go to **APIs & Services** → **Credentials**
   - Click **Create Credentials** → **OAuth client ID**
   - Choose **Desktop App**
   - Download the `credentials.json` file and place it in your project folder.

3. **Google Sheet Setup:**
   - Create a new Google Sheet.
   - Copy its **Sheet ID** from the URL and update it in the script (`SPREADSHEET_ID` variable).
   - Share the sheet with the Google account you use to authenticate (the one that appears in `token.json` after the first run).

4. **Run the Script:**
   - Use the following command:
     ```bash
     python email_to_sheet.py
     ```
   - A browser window will open asking you to sign in with your Google account and authorize access.
   - A file named `token.json` will be created automatically for future authentication.


---

## 🧪 Example Output in Google Sheet

| Date & Time         | From                | Subject             | Body Snippet              | Message ID     |
|---------------------|---------------------|----------------------|----------------------------|----------------|
| 2025-06-20 09:12:00 | someone@example.com | Welcome to our app! | Hello Bhavya, thanks for... | 17c4e5abccaa1  |

---

## 🛠 Configuration

Edit these lines in `email_to_sheet.py` to set your target spreadsheet:

```python
SPREADSHEET_ID = 'your-google-sheet-id-here'
RANGE_NAME = 'Sheet1!A:E'
```
---

## ⚠️ Notes

- Only messages from the inbox are fetched (`labelIds=['INBOX']`).
- The script retrieves the 10 most recent emails each time it runs.
- The email body is extracted from either plain text or HTML and is trimmed to 200 characters for readability.
- Data is **appended** to the specified Google Sheet — make sure to handle duplicates manually if needed.
- A `token.json` file is created after the first run to store your authentication session.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with 💻 by [Bhavya Kanojia](https://github.com/XxBHAVYAxX)


