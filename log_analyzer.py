import re
import sys
from collections import defaultdict

def analyze_logs(log_file):
    # Pattern to detect failed login attempts
    failed_login_pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

    failed_attempts = defaultdict(int)

    try:
        with open(log_file, "r") as file:
            for line in file:
                match = failed_login_pattern.search(line)
                if match:
                    ip = match.group(1)
                    failed_attempts[ip] += 1
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
        return

    print("\nSecurity Log Analysis Report")
    print("-----------------------------")

    suspicious_found = False

    for ip, attempts in failed_attempts.items():
        if attempts >= 3:
            suspicious_found = True
            print("⚠️  Suspicious Activity Detected")
            print(f"IP Address: {ip}")
            print(f"Failed Attempts: {attempts}")
            print()

    if not suspicious_found:
        print("No suspicious login attempts detected.")

def main():
    print("Security Log Analyzer")
    print("----------------------")

    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    else:
        log_file = "auth.log"

    print(f"Analyzing log file: {log_file}")
    analyze_logs(log_file)

if __name__ == "__main__":
    main()
