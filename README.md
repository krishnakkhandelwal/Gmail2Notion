# mail2notion 🚀

**mail2notion** is a lightweight Python project designed to automate extracting actionable items from your Gmail inbox and syncing them into **Notion** as tasks or notes.  
It combines **NLP, OCR, and ML** to ensure no important task or deadline is missed.

---

## 📌 Problem Statement
Important tasks hidden in emails and image attachments are often overlooked due to inbox overload.  
Manual tracking wastes time, risks deadlines, and adds unnecessary friction.

---

## ⚡ Why mail2notion?
- Emails often contain implicit or relative deadlines that tools like Gmail/Outlook reminders miss.  
- Manual copy-pasting tasks from emails into Notion is repetitive and error-prone.  
- By integrating Gmail with Notion, you get a **centralized, organized workspace** to manage commitments efficiently.  

**Result →** Save time ⏳, reduce errors ✅, boost productivity 📈.

---

## 🛠 What does mail2notion do?
- Connects to your **Gmail inbox** via Gmail API.
- Extracts key email details: **subject, sender, date, message body**.
- Applies **data preprocessing + ML/NLP/OCR models** to detect:
  - Deadlines (explicit & relative)  
  - Tasks hidden in email text or image attachments  
- Syncs results to **Notion** via API, creating/updating task entries automatically.

---

## 🏗 System Architecture
1. **Gmail API** → Fetch emails.  
2. **Data Preprocessing** → Clean and structure email data.  
3. **ML Model (NLP + OCR + Classifier)** → Extract tasks, dates, and context.  
4. **Notion API** → Store structured tasks in Notion database.  

---

## 🔑 Features & Novelty
- Seamless handling of **email text + image attachments**.  
- **Fully automated pipeline**: extraction → categorization → Notion sync.
- Advanced classification for task prioritization (urgent, follow-up, low priority). 
- Works beyond explicit calendar events, tackling **implicit deadlines & contextual cues**.  
- **End-to-end workflow** → no manual intervention needed.

---

## 📚 Future Scope
- Support for multiple email providers (Outlook, Yahoo, etc.).  
- Integration with other productivity apps (Trello, Slack, Google Calendar).
- Integration with Device Clock & Calendar (Setup of Alarms and Reminders)

---

## 👩‍💻 Team Members
- Shambhavee Gune  
- Dnyaneshwari Kale  
- Alvin Jiju  
- Krishna Khandelwal  

---

## 🚀 Getting Started
Check the [INSTALLATION.md](./INSTALLATION.md) file for setup, dependencies, and usage instructions.

---

*Created by Krishna Khandelwal and team.*
