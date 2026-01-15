import argparse
from src.parser import parse_log_file, detect_bruteforce, write_report



def main():
    parser = argparse.ArgumentParser(
        description="Security Log Analyzer - Brute Force Detection"
    )

    parser.add_argument(
        "--file",
        default="logs/sample.log",
        help="Path to log file"
    )

    parser.add_argument(
        "--threshold",
        type=int,
        default=3,
        help="Failed login threshold for brute-force detection"
    )

    args = parser.parse_args()

    entries = parse_log_file(args.file)

    print(f"Parsed {len(entries)} log entries\n")

    for entry in entries:
        print(
            f"{entry['timestamp']} | "
            f"{entry['ip']} | "
            f"{entry['status']}"
        )

    print("\n--- Security Analysis ---")
    print(f"Brute-force threshold: {args.threshold}\n")

    alerts = detect_bruteforce(entries, args.threshold)

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
