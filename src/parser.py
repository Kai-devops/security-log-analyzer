import re


def parse_log_file(filepath):
    entries = []

    log_pattern = re.compile(
        r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
        r"IP=(?P<ip>\d+\.\d+\.\d+\.\d+) "
        r"STATUS=(?P<status>\w+)"
    )

    with open(filepath, "r") as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                entries.append(match.groupdict())

    return entries

from collections import Counter


def detect_bruteforce(entries, threshold=3):
    failed_ips = []

    for entry in entries:
        if entry["status"] == "FAIL":
            failed_ips.append(entry["ip"])

    counts = Counter(failed_ips)

    suspicious = {
        ip: count
        for ip, count in counts.items()
        if count >= threshold
    }

    return suspicious

def write_report(alerts, filepath="report.txt"):
    with open(filepath, "w", encoding="utf-8") as file:

        if not alerts:
            file.write("No suspicious activity detected.\n")
            return

        file.write("Potential brute-force attempts detected:\n\n")
        for ip, count in alerts.items():
            file.write(f"IP {ip} → {count} failed attempts\n")
