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
