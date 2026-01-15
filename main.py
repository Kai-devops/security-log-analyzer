from src.parser import parse_log_file, detect_bruteforce, write_report


def main():
    log_file = "logs/sample.log"
    threshold = 3
    entries = parse_log_file(log_file)

    print(f"Parsed {len(entries)} log entries\n")

    for entry in entries:
        print(
            f"{entry['timestamp']} | "
            f"{entry['ip']} | "
            f"{entry['status']}"
        )

    print("\n--- Security Analysis ---")
    print(f"Brute-force threshold: {threshold} failed attempts\n")

    alerts = detect_bruteforce(entries, threshold)

    if alerts:
        print("⚠️  Potential brute-force attempts detected:\n")
        for ip, count in alerts.items():
            print(f"IP {ip} → {count} failed attempts")
    else:
        print("No suspicious activity detected.")

    write_report(alerts)
    print("\nReport written to report.txt")



if __name__ == "__main__":
    main()
