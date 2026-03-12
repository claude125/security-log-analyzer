# Security Log Analyzer

A Python-based tool designed to analyze Linux system and security logs to detect suspicious activity and potential security threats.

This tool helps system administrators and security engineers identify abnormal login behavior, repeated authentication failures, and possible intrusion attempts by analyzing system log files.

---

## Overview

System logs contain valuable security information. By analyzing authentication logs, administrators can detect potential brute-force attacks, unauthorized login attempts, and other suspicious activities.

The Security Log Analyzer reads log files and highlights suspicious patterns such as multiple failed login attempts from the same IP address.

---

## Features

- Analyze Linux authentication logs
- Detect repeated failed login attempts
- Identify suspicious IP addresses
- Highlight potential brute-force attacks
- Simple command-line interface
- Lightweight and easy to deploy

---

## Technologies Used

- Python
- Regular Expressions (regex)
- Linux system logs
- Cybersecurity log analysis techniques

---

## Example Logs Analyzed
/var/log/auth.log
/var/log/syslog
/var/log/secure

These logs contain authentication events, login attempts, and security-related activities.

---

## Example Output
WARNING: Multiple failed login attempts detected

IP Address: 192.168.1.25
Attempts: 6

This output indicates that the system detected multiple failed login attempts from a single IP address, which may suggest a brute-force attack.

---

## Installation

Clone the repository:
git clone https://github.com/claude125/security-log-analyzer.git

Navigate into the project directory:
cd security-log-analyzer
Install required dependencies:


pip install -r requirements.txt


---

## Running the Tool

Run the log analyzer script:


python log_analyzer.py


The script will scan the log file and report suspicious login attempts.

---

## Project Structure


security-log-analyzer
│
├── README.md
├── log_analyzer.py
└── requirements.txt


---

## Use Cases

This tool can be useful for:

- System administrators monitoring server security
- Security engineers detecting brute-force login attempts
- DevOps teams monitoring authentication logs
- Cybersecurity students learning about log analysis

---

## Future Improvements

Possible future enhancements include:

- Real-time log monitoring
- Email alerts for suspicious activity
- Machine learning anomaly detection
- Dashboard visualization for security events
- Integration with SIEM systems
- Support for additional log formats

---

## Author

Claude Dusengimana  
Senior Network & Security Engineer  
Kigali, Rwanda

LinkedIn: https://linkedin.com/in/dusengimana-claude  
GitHub: https://github.com/claude125

The tool can analyze logs such as:
