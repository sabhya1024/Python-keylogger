# Python-keylogger
# 🕵️ Modular Python Keylogger

> 🔒 **For educational and ethical use only.** Do not deploy this on systems you don't own or have explicit permission to monitor.

A modular keylogger written in Python that collects clipboard content, system information, keystrokes, and screenshots, encrypts the text data using Base64, and sends it all as email attachments.

---

## 📁 Project Structure

KEYLOGGER/
├── main.py               # Main script: runs the whole logic
├── clipboard.py          # Captures clipboard text
├── key_log.py            # Logs keystrokes to file (keylog_info.txt)
├── system_info.py        # Gathers system details
├── screenshot.py         # Takes a screenshot
├── encryption.py         # Encrypts text with Base64
├── mail.py               # Sends email with attachments
└── README.md             # This file

some files will be created when you will run the project

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

        pip install pynput mss


### 2. Configure email settings
fromaddr = "your_email@gmail.com"
toaddr = "receiver_email@gmail.com"
password = "your_app_password"


---

There is a timer which decides the amount of time interval in which it has to send the mail.



