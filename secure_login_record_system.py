import os
import re
import csv
import json
import hashlib
import logging
import shutil
from datetime import datetime, date, timedelta

DATA_DIR = "data"
LOG_DIR = "logs"
ARCHIVE_DIR = "archive"

USERS_FILE = f"{DATA_DIR}/users.json"
LOGIN_TXT_FILE = f"{DATA_DIR}/login_records.txt"
FAILED_CSV_FILE = f"{DATA_DIR}/failed_attempts.csv"
BLOCKED_JSON_FILE = f"{DATA_DIR}/blocked_users.json"
SESSION_CSV_FILE = f"{DATA_DIR}/session_history.csv"
SUSPICIOUS_LOG_FILE = f"{LOG_DIR}/suspicious_activity.log"

users = {}
failed_attempts = {}
blocked_users = set()


def create_directories():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(ARCHIVE_DIR, exist_ok=True)


def get_daily_log_file():
    today = date.today().strftime("%Y-%m-%d")
    return f"{LOG_DIR}/activity_{today}.log"


def setup_logging():
    logging.basicConfig(
        filename=get_daily_log_file(),
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def validate_username(username):
    pattern = r"^[a-zA-Z0-9_.]+@university\.edu$"
    return re.match(pattern, username) is not None


def validate_password(password):
    return (
        len(password) >= 8
        and re.search(r"[A-Z]", password)
        and re.search(r"[a-z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r"[@#$%^&+=!]", password)
    )


def load_users():
    global users

    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as file:
                users = json.load(file)
        else:
            users = {}
    except Exception as error:
        logging.error(f"Error loading users: {error}")
        users = {}


def save_users():
    try:
        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=4)
    except Exception as error:
        logging.error(f"Error saving users: {error}")


def load_blocked_users():
    global blocked_users

    try:
        if os.path.exists(BLOCKED_JSON_FILE):
            with open(BLOCKED_JSON_FILE, "r") as file:
                blocked_users = set(json.load(file))
        else:
            blocked_users = set()
    except Exception as error:
        logging.error(f"Error loading blocked users: {error}")
        blocked_users = set()


def save_blocked_users():
    try:
        with open(BLOCKED_JSON_FILE, "w") as file:
            json.dump(list(blocked_users), file, indent=4)
    except Exception as error:
        logging.error(f"Error saving blocked users: {error}")


def write_login_record(username, status):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOGIN_TXT_FILE, "a") as file:
            file.write(f"{timestamp} | {username} | {status}\n")

        logging.info(f"{username} | {status}")

    except Exception as error:
        logging.error(f"Error writing login record: {error}")


def write_failed_attempt(username, reason):
    try:
        file_exists = os.path.exists(FAILED_CSV_FILE)

        with open(FAILED_CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["timestamp", "username", "reason"])

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                username,
                reason
            ])

        with open(SUSPICIOUS_LOG_FILE, "a") as file:
            file.write(f"{datetime.now()} | {username} | {reason}\n")

        logging.warning(f"Suspicious activity: {username} | {reason}")

    except Exception as error:
        logging.error(f"Error writing failed attempt: {error}")


def write_session_history(username, action):
    try:
        file_exists = os.path.exists(SESSION_CSV_FILE)

        with open(SESSION_CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["timestamp", "username", "session_action"])

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                username,
                action
            ])

        logging.info(f"Session action: {username} | {action}")

    except Exception as error:
        logging.error(f"Error writing session history: {error}")


def register_user():
    try:
        username = input("Enter university email: ").strip()
        password = input("Enter password: ").strip()

        if not validate_username(username):
            print("Invalid username format. Use name@university.edu")
            write_failed_attempt(username, "INVALID_USERNAME_FORMAT")
            return

        if not validate_password(password):
            print("Weak password.")
            write_failed_attempt(username, "WEAK_PASSWORD")
            return

        users[username] = hash_password(password)
        failed_attempts[username] = 0

        save_users()
        write_login_record(username, "USER_REGISTERED")

        print("User registered successfully.")

    except Exception as error:
        logging.error(f"Registration error: {error}")
        print("Error occurred during registration.")


def login_user():
    try:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if username in blocked_users:
            print("Account is blocked.")
            write_failed_attempt(username, "BLOCKED_LOGIN_ATTEMPT")
            return

        if username not in users:
            print("User not found.")
            write_failed_attempt(username, "UNKNOWN_USER_ATTEMPT")
            return

        if users[username] == hash_password(password):
            print("Login successful.")
            failed_attempts[username] = 0
            write_login_record(username, "LOGIN_SUCCESS")
            session_manager(username)
        else:
            failed_attempts[username] = failed_attempts.get(username, 0) + 1
            print("Invalid password.")
            write_failed_attempt(username, "LOGIN_FAILED")

            if failed_attempts[username] >= 3:
                blocked_users.add(username)
                save_blocked_users()
                write_failed_attempt(username, "ACCOUNT_BLOCKED")
                print("Account blocked after 3 failed attempts.")

    except Exception as error:
        logging.error(f"Login error: {error}")
        print("Error occurred during login.")


def session_manager(username):
    try:
        print("Session started.")
        write_session_history(username, "SESSION_STARTED")

        session_start = datetime.now()
        timeout_seconds = 15

        while True:
            action = input("Enter action [resource/logout/wait]: ").lower().strip()

            elapsed_time = (datetime.now() - session_start).total_seconds()

            if elapsed_time > timeout_seconds:
                print("Session timeout.")
                write_session_history(username, "SESSION_TIMEOUT")
                write_login_record(username, "SESSION_TIMEOUT")
                break

            if action == "resource":
                print("Student resource accessed.")
                write_session_history(username, "RESOURCE_ACCESSED")

            elif action == "logout":
                print("Logged out successfully.")
                write_session_history(username, "LOGOUT")
                write_login_record(username, "LOGOUT")
                break

            elif action == "wait":
                print("Waiting...")

            else:
                print("Invalid action.")
                write_session_history(username, "INVALID_SESSION_ACTION")

    except Exception as error:
        logging.error(f"Session error: {error}")
        print("Session error occurred.")


def export_summary_report():
    try:
        report = {
            "total_users": len(users),
            "blocked_users": list(blocked_users),
            "failed_attempts": failed_attempts,
            "report_generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        report_file = f"{DATA_DIR}/security_summary_report.json"

        with open(report_file, "w") as file:
            json.dump(report, file, indent=4)

        print(f"Security summary report generated: {report_file}")
        logging.info("Security summary report generated.")

    except Exception as error:
        logging.error(f"Report generation error: {error}")
        print("Error generating report.")


def archive_old_logs():
    try:
        today = date.today()

        for filename in os.listdir(LOG_DIR):
            file_path = os.path.join(LOG_DIR, filename)

            if filename.startswith("activity_") and filename.endswith(".log"):
                date_part = filename.replace("activity_", "").replace(".log", "")
                log_date = datetime.strptime(date_part, "%Y-%m-%d").date()

                if log_date < today:
                    shutil.move(file_path, os.path.join(ARCHIVE_DIR, filename))
                    logging.info(f"Archived old log file: {filename}")

        print("Old log files archived successfully.")

    except Exception as error:
        logging.error(f"Log archival error: {error}")
        print("Error while archiving logs.")


def display_files_created():
    print("\nFiles Created / Updated")
    print("-----------------------")
    print(USERS_FILE)
    print(LOGIN_TXT_FILE)
    print(FAILED_CSV_FILE)
    print(BLOCKED_JSON_FILE)
    print(SESSION_CSV_FILE)
    print(SUSPICIOUS_LOG_FILE)
    print(get_daily_log_file())


def main():
    create_directories()
    setup_logging()
    load_users()
    load_blocked_users()

    while True:
        print("\nSecure University Login Record Management System")
        print("1. Register User")
        print("2. Login")
        print("3. Generate Security Summary Report")
        print("4. Archive Old Logs")
        print("5. Show Files Created")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            export_summary_report()
        elif choice == "4":
            archive_old_logs()
        elif choice == "5":
            display_files_created()
        elif choice == "6":
            print("System closed.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
