# Security Log Analyzer 🔐

A Python-based command-line tool that analyzes authentication-style log files to detect potential brute-force login attempts.

This project simulates **SOC (Security Operations Center)** analysis by parsing logs, identifying repeated failed login attempts, and generating a security report.

---

## Features
- Parses structured log files using regex
- Extracts timestamps, IP addresses, and login status
- Detects potential brute-force attacks using a configurable threshold
- Generates a security report (`report.txt`)
- Command-line arguments for flexibility

---

## Project Structure
security-log-analyzer/
│
├── logs/
│ └── sample.log
│
├── src/
│ └── parser.py
│
├── main.py
├── README.md
└── .gitignore


---

## Sample Log Format
2025-01-10 08:14:22 IP=192.168.1.10 STATUS=FAIL


---

## How It Works
1. Log entries are parsed using regular expressions
2. Failed login attempts are counted per IP address
3. If an IP exceeds the configured failure threshold, it is flagged
4. Results are displayed in the CLI and written to a report file

---

## Usage

### Run with default settings
```bash
python main.py

## Specify custom threshold
python main.py --threshold 3

## specify a different log file
python main.py --file logs/sample.log --threshold 4

##Output
outputs in a simple report.txt file containing alert details.


##Technologies Used
Python 3
Regular Expressions (re)
argparse
collections.Counter


##Security Concepts Demonstrated
Log analysis
Brute-force detection
Threshold-based alerting
SOC-style reporting

Secure file handling (UTF-8 encoding)
##Future Improvements
CSV / JSON report export
Support for multiple log formats
Time-based detection windows
Integration with SIEM tools

Author
Kai
GitHub: https://github.com/kai-devops