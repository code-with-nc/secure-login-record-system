# Secure University Login Record Management System

## 🔐 Secure Authentication • 📁 Persistent Storage • 📊 Audit Logging • 🛡️ Security Monitoring

A Python-based secure login record management and audit trail system designed for university security monitoring, forensic logging, persistent storage, and structured reporting.

This project extends the Day 1 Secure Login System by integrating advanced file handling operations, automated logging, CSV/JSON processing, session record management, and forensic-style audit trail generation similar to enterprise cyber security and monitoring systems.

</div>

---

# ✨ Features

## 🔑 Authentication & Security

* ✅ Secure university email validation
* ✅ Strong password complexity validation
* ✅ SHA-256 password hashing
* ✅ Failed login attempt tracking
* ✅ Automatic account blocking after 3 failed attempts
* ✅ Session timeout monitoring

---

## 📁 File Handling & Storage

* ✅ Persistent user database storage
* ✅ TXT report generation
* ✅ CSV report generation
* ✅ JSON report generation
* ✅ Structured forensic logging
* ✅ Daily automated log creation
* ✅ Automatic archival of old logs

---

## 📊 Monitoring & Reporting

* ✅ Suspicious activity logging
* ✅ Security summary report generation
* ✅ Session activity monitoring
* ✅ Security audit trail maintenance
* ✅ Exception handling using logging module

---

# 🛠️ Technologies Used

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python 3   | Core Programming            |
| hashlib    | Password Hashing            |
| csv        | CSV File Processing         |
| json       | JSON Serialization          |
| datetime   | Timestamp & Date Handling   |
| logging    | Automated Logging           |
| os         | File & Directory Operations |
| shutil     | Log Archival                |
| re         | Input Validation            |

---

# 🎯 Objectives

This laboratory exercise helps students understand:

* Advanced file handling techniques
* CSV and JSON processing
* Persistent application storage
* Logging and monitoring systems
* Security audit trail management
* Data serialization and parsing
* Automated reporting systems
* Runtime exception handling
* Forensic-style logging workflows

---

# 📂 Project Structure

```text
secure-login-record-system/
│
├── secure_login_record_system.py
├── README.md
│
├── data/
│   ├── users.json
│   ├── login_records.txt
│   ├── failed_attempts.csv
│   ├── blocked_users.json
│   ├── session_history.csv
│   └── security_summary_report.json
│
├── logs/
│   ├── activity_YYYY-MM-DD.log
│   └── suspicious_activity.log
│
└── archive/
```

---

# ⚙️ Functional Modules

## 🔐 Authentication Module

* Validates university email format
* Validates strong passwords
* Hashes passwords using SHA-256
* Verifies login credentials

---

## 💾 Persistent Storage Module

Stores:

* User database
* Failed attempts
* Session history
* Blocked users
* Security reports

---

## 📜 Logging Module

Maintains:

* Daily activity logs
* Suspicious activity logs
* Session timeout logs
* Security audit trails

---

## 📊 Reporting Module

Generates:

* TXT reports
* CSV reports
* JSON reports
* Security summary reports

---

## 📦 Archival Module

Automatically archives old activity log files into the archive directory.

---

# 📄 Output Files

## TXT Files

* `login_records.txt`

## CSV Files

* `failed_attempts.csv`
* `session_history.csv`

## JSON Files

* `users.json`
* `blocked_users.json`
* `security_summary_report.json`

## Log Files

* `activity_YYYY-MM-DD.log`
* `suspicious_activity.log`

---

# 🐉 Run on Kali Linux

```bash
sudo apt update

sudo apt install python3 -y

mkdir secure-login-record-system

cd secure-login-record-system

nano secure_login_record_system.py

python3 secure_login_record_system.py
```

---

# 🚀 GitHub Push Commands

```bash
git init

git add .

git commit -m "Add secure login record management system"

git branch -M main

git remote add origin https://github.com/code-with-nc/secure-login-record-system.git

git push -u origin main
```

---

# 🔍 Security Observations

* 🔒 Passwords are never stored in plain text.
* 🔒 SHA-256 hashing secures credentials.
* 📊 Failed login attempts are permanently recorded.
* 🚨 Suspicious activities are monitored separately.
* 🕒 Session activities are preserved for investigation.
* 📁 Daily logs improve forensic traceability.
* 💾 Persistent storage enables long-term monitoring.
* 📦 Automatic archival improves log management.
* ⚠️ Exception handling improves application reliability.

---

# 🚀 Future Enhancements

* SQLite/MySQL database integration
* bcrypt or Argon2 hashing
* Flask-based web dashboard
* OTP-based authentication
* Role-based access control
* Real-time monitoring dashboard
* Docker containerization
* REST API integration
* Cloud deployment support
* Email alert system for suspicious activity

---

<div align="center">

## 🛡️ Educational Cyber Security & File Handling Laboratory Project

Developed for advanced Python programming, secure file handling, forensic logging, and security monitoring practice.

</div>
