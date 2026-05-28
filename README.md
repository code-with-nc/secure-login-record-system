````md
# Secure University Login Record Management System

A Python-based secure login record management and audit trail system developed for university security monitoring, forensic logging, persistent storage, and structured reporting.

This project extends the Day 1 Secure Login System by integrating advanced file handling operations, automated logging, CSV/JSON processing, session record management, and forensic-style audit trail generation similar to enterprise cyber security and monitoring systems.

---

# Features

- Secure university email validation
- Strong password complexity validation
- SHA-256 password hashing
- Persistent user database storage
- Failed login attempt tracking
- Automatic account blocking after 3 failed attempts
- Session activity monitoring
- Session timeout recording
- TXT, CSV, and JSON report generation
- Daily automated log file creation
- Suspicious activity logging
- Security summary report generation
- Automatic archival of old logs
- Exception handling using logging module
- Structured audit trail maintenance

---

# Technologies Used

- Python 3
- hashlib
- csv
- json
- datetime
- logging
- os
- shutil
- re

---

# Objectives

This laboratory exercise helps students understand:

- Advanced file handling techniques
- CSV and JSON processing
- Persistent application storage
- Logging and monitoring systems
- Security audit trail management
- Data serialization and parsing
- Automated reporting systems
- Runtime exception handling
- Forensic-style logging workflows

---

# Project Structure

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

# Functional Modules

## Authentication Module

- Validates university email format
- Validates strong passwords
- Hashes passwords using SHA-256
- Verifies login credentials

## Persistent Storage Module

Stores:

- User database
- Failed attempts
- Session history
- Blocked users
- Security reports

## Logging Module

Maintains:

- Daily activity logs
- Suspicious activity logs
- Session timeout logs
- Security audit trails

## Reporting Module

Generates:

- TXT reports
- CSV reports
- JSON reports
- Security summary reports

## Archival Module

Automatically archives old activity log files into archive directory.

---

# Output Files

## TXT Files

- login_records.txt

## CSV Files

- failed_attempts.csv
- session_history.csv

## JSON Files

- users.json
- blocked_users.json
- security_summary_report.json

## Log Files

- activity_YYYY-MM-DD.log
- suspicious_activity.log

---

# Run on Kali Linux

```bash
sudo apt update

sudo apt install python3 -y

mkdir secure-login-record-system

cd secure-login-record-system

nano secure_login_record_system.py

python3 secure_login_record_system.py
```

---

# GitHub Push Commands

```bash
git init

git add .

git commit -m "Add secure login record management system"

git branch -M main

git remote add origin https://github.com/code-with-nc/secure-login-record-system.git

git push -u origin main
```

---

# Security Observations

- Passwords are never stored in plain text.
- SHA-256 hashing secures credentials.
- Failed login attempts are permanently recorded.
- Suspicious activities are monitored separately.
- Session activities are preserved for investigation.
- Daily logs improve forensic traceability.
- Persistent storage enables long-term monitoring.
- Automatic archival improves log management.
- Exception handling improves application reliability.

---

# Future Enhancements

- SQLite/MySQL database integration
- bcrypt or Argon2 hashing
- Flask-based web dashboard
- OTP-based authentication
- Role-based access control
- Real-time monitoring dashboard
- Docker containerization
- REST API integration
- Cloud deployment support
- Email alert system for suspicious activity
````
