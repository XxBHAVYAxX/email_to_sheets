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
