<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=0:030712,50:1a0a00,100:ff4757&height=200&section=header&text=Security%20Log%20Analyzer&fontSize=46&fontColor=ffffff&fontAlignY=38&desc=Python-Powered%20Linux%20Log%20Analysis%20%26%20Intrusion%20Detection&descSize=15&descAlignY=58&animation=fadeIn)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=14&pause=1500&color=FF4757&center=true&vCenter=true&width=750&height=40&lines=🔍+Detect+Brute-Force+Attacks+in+Real+Time;🚨+Identify+Suspicious+IP+Addresses+Instantly;📋+Analyze+auth.log+%2F+syslog+%2F+secure;🛡️+Built+for+SysAdmins+%26+Security+Engineers;⚡+Lightweight+CLI+—+Zero+Dependencies+Overhead)](https://git.io/typing-svg)

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Regex](https://img.shields.io/badge/Regex-Pattern_Matching-ff4757?style=for-the-badge&logoColor=white)
![Security](https://img.shields.io/badge/Cybersecurity-Log_Analysis-9FEF00?style=for-the-badge&logo=hackthebox&logoColor=black)
![SIEM](https://img.shields.io/badge/SIEM-Ready-660066?style=for-the-badge&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-Tool-0d1117?style=for-the-badge&logo=windowsterminal&logoColor=white)

</div>

---

## 🔍 What Is This?

Your Linux server logs are recording attacks **right now** — failed SSH logins, brute-force sweeps, unauthorized access attempts. Most go unnoticed until it's too late.

The **Security Log Analyzer** cuts through the noise. It parses your authentication logs, surfaces suspicious patterns, and flags potential intrusion attempts — all from a single Python script you can run in seconds.

Built for **system administrators, security engineers, and DevOps teams** who need fast, actionable intelligence from raw log data.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **Auth Log Analysis** | Parses `/var/log/auth.log`, `/var/log/secure`, `/var/log/syslog` |
| 🔁 **Brute-Force Detection** | Flags IPs with repeated failed login attempts |
| 🌐 **Suspicious IP Identification** | Groups and ranks attacking IP addresses by attempt count |
| 🚨 **Threshold-Based Alerts** | Configurable warning triggers for failed attempt counts |
| 📊 **Attack Summary Report** | Clean, readable terminal output with severity levels |
| ⚡ **Lightweight CLI** | No heavy dependencies — runs anywhere Python runs |

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/claude125/security-log-analyzer.git
cd security-log-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the analyzer
python log_analyzer.py
```

---

## 📋 Log Files Analyzed

```bash
/var/log/auth.log     # Debian / Ubuntu — SSH & auth events
/var/log/secure       # RHEL / CentOS   — authentication logs
/var/log/syslog       # General system events & errors
```

---

## 📊 Example Output

```
╔══════════════════════════════════════════════════════════════╗
║              SECURITY LOG ANALYZER  v1.0                     ║
║              Scan started: 2025-03-13  14:45:02  UTC+2       ║
╠══════════════════════════════════════════════════════════════╣
║  📋 Log File : /var/log/auth.log                             ║
║  📦 Lines    : 18,432  parsed                                ║
║  ⏱️  Duration  : 0.83 seconds                                ║
╠══════════════════════════════════════════════════════════════╣
║  🌐 SUSPICIOUS IP REPORT                                     ║
║                                                              ║
║  Rank  IP Address        Attempts   Severity                 ║
║  ─────────────────────────────────────────────              ║
║  [1]   203.0.113.47      142        🔴 CRITICAL              ║
║  [2]   198.51.100.22      87        🔴 CRITICAL              ║
║  [3]   192.168.1.25       34        🟠 HIGH                  ║
║  [4]   10.0.0.88          12        🟡 MEDIUM                ║
║  [5]   172.16.0.5          7        🟡 MEDIUM                ║
╠══════════════════════════════════════════════════════════════╣
║  🚨 ALERTS                                                   ║
║                                                              ║
║  [CRITICAL] 203.0.113.47  — 142 failed SSH attempts          ║
║             Possible automated brute-force attack            ║
║                                                              ║
║  [CRITICAL] 198.51.100.22 — 87 failed SSH attempts           ║
║             Possible credential stuffing attack              ║
║                                                              ║
║  [HIGH]     192.168.1.25  — 34 failed SSH attempts           ║
║             Repeated authentication failure detected         ║
╠══════════════════════════════════════════════════════════════╣
║  📈 SUMMARY                                                  ║
║  Total suspicious IPs   : 5                                  ║
║  Total failed attempts  : 282                                ║
║  Critical alerts        : 2                                  ║
║  Recommended action     : Block IPs via firewall / fail2ban  ║
╚══════════════════════════════════════════════════════════════╝
```

---

## ⚙️ Configuration

```python
# Tune detection sensitivity in log_analyzer.py

THRESHOLDS = {
    "medium"   : 5,    # 5+ failures   → Medium alert
    "high"     : 20,   # 20+ failures  → High alert
    "critical" : 50,   # 50+ failures  → Critical alert
}

LOG_FILES = [
    "/var/log/auth.log",
    "/var/log/secure",
    "/var/log/syslog",
]
```

---

## 🧰 Tech Stack

```
Python 3.x         — Core scripting language
re (regex)         — Log pattern matching & extraction
collections        — IP address frequency counting
datetime           — Timestamp parsing & formatting
argparse           — CLI argument handling
```

---

## 📁 Project Structure

```
security-log-analyzer/
│
├── 📄 log_analyzer.py     # Main analysis engine
├── 📄 requirements.txt    # Python dependencies
└── 📄 README.md
```

---

## 🌍 Who Is This For?

`🖥️ SysAdmins` &nbsp; `🔐 Security Engineers` &nbsp; `☁️ DevOps Teams` &nbsp; `🎓 Cybersecurity Students` &nbsp; `🏢 IT Operations`

---

## 🚀 Roadmap

```python
roadmap = [
    "👁️  Real-time log monitoring with inotify",
    "📧 Email & Slack alerts for critical events",
    "🧠 ML-based anomaly detection for zero-day patterns",
    "📊 Web dashboard for security event visualization",
    "🔗 SIEM integration (Splunk / ELK Stack)",
    "🌍 GeoIP lookup for attacking IP geolocation",
    "📝 Support for Apache / Nginx / Windows Event logs",
]
```

---

## 👤 Author

<div align="center">

**Claude Dusengimana**
*Senior Network & Security Engineer | IoT Researcher*
📍 Kigali, Rwanda

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/dusengimana-claude)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-161b22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/claude125)
[![Gmail](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dusenge125@gmail.com)

</div>

---

<div align="center">

![footer](https://capsule-render.vercel.app/api?type=waving&color=0:ff4757,50:1a0a00,100:030712&height=100&section=footer&text=Know+your+logs.+Know+your+enemy.&fontSize=14&fontColor=ffffff&fontAlignY=65&animation=fadeIn)

*⭐ Star this repo if it helped you catch an attack — or avoid one.*

</div>
