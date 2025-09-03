# Installation Guide for mail2notion

This guide will help you set up and run the mail2notion project to extract your emails and prepare for Notion integration.

---

## Prerequisites

- **Python 3.7 or higher**
- A **Google account** with Gmail
- Access to **Google Cloud Console**
- Internet connection (for API access)

---

## Step 1: Clone the Repository


git clone <your-repo-url>
cd mail2notion


---

## Step 2: Create and Activate a Python Virtual Environment

python3 -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate       # Windows


---

## Step 3: Install Dependencies

Install all required Python packages using pip:

```
pip install -r requirements.txt
```


---

## Step 4: Google Cloud Setup and Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. **Create a new project** (or select an existing one).
3. Under **APIs & Services > Library**, enable **Gmail API** for your project.
4. Under **APIs & Services > OAuth consent screen**:
    - Set **User type** to External.
    - Fill out **App Information** (name, support email).
    - **Add your Google account as a Test User** for the app.
5. Under **APIs & Services > Credentials**:
    - Create **OAuth Client ID** (type: Desktop).
    - Download the `credentials.json` file.
    - Place `credentials.json` in your project root directory.
6. **Do NOT upload `credentials.json` or `token.json` to Github**.

---

## Step 5: Run the Email Extraction Script

```
python extract_emails.py
```

- On first run, a browser window will open to authenticate with Google and grant Gmail API access.
- After authentication, a `token.json` file is created for future use.
- Emails will be printed in your console.

---

## Troubleshooting

- If you get "403 access denied":  
  - Ensure you added your Gmail account as a Test User in the OAuth consent screen.
- If port issues occur during authentication:
  - Edit the script to use a different port (e.g. `creds = flow.run_local_server(port=8081)`).
  - Or use `flow.run_console()` for manual authentication.

---

## Next Steps

- You can now process extracted emails, apply NLP, or push data into Notion using the Notion API.
- Extend the script as your workflow evolves!

---

*For project and usage details, read the README.md file.*
```

***

Feel free to copy-paste and adjust `<your-repo-url>` as needed! This is ready to be added as `INSTALLATION.md` in your repo.

[1](https://realpython.com/installing-python/)
[2](https://www.youtube.com/watch?v=3JHlILId9-k)
[3](https://docs.python.org/3/using/index.html)
[4](https://www.youtube.com/watch?v=NES0LRUFMBE)
[5](https://www.youtube.com/watch?v=NfTrFhfqmFY)
[6](https://kinsta.com/knowledgebase/install-python/)
[7](https://www.pluralsight.com/resources/blog/software-development/python-installation-guide)
[8](https://www.youtube.com/watch?v=hvX7NGk2Ca0)
[9](https://packaging.python.org/tutorials/installing-packages/)
[10](https://docs.python-guide.org/starting/installation/)
