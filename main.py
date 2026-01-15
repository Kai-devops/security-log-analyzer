from src.parser import parse_log_file, detect_bruteforce


def main():
    log_file = "logs/sample.log"
    entries = parse_log_file(log_file)

    print(f"Parsed {len(entries)} log entries\n")

    for entry in entries:
        print(
            f"{entry['timestamp']} | "
            f"{entry['ip']} | "
            f"{entry['status']}"
        )

    print("\n--- Security Analysis ---")

    alerts = detect_bruteforce(entries)

    if alerts:
        print("⚠️  Potential brute-force attempts detected:\n")
        for ip, count in alerts.items():
            print(f"IP {ip} → {count} failed attempts")
    else:
        print("No suspicious activity detected.")


if __name__ == "__main__":
    main()
