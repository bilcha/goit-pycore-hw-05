import sys
import re
from typing import List, Dict

def parse_log_line(line: str) -> Dict:
    parts = line.strip().split(maxsplit=3)
    if len(parts) == 4:
        return {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": parts[3],
        }
    return {}

def load_logs(file_path: str) -> List[Dict]:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Read file error: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    level = level.upper()
    return [log for log in logs if log["level"] == level]

def count_logs_by_level(logs: List[Dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    print("\nLevel | Quantity")
    print("-----------------|----------")
    for level, count in sorted(counts.items()):
        print(f"{level:<17}| {count}")

def display_filtered_logs(logs: List[Dict], level: str):
    print(f"\nLogs for '{level}' level:")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("python3 main.py logfile.log")
        sys.exit(1)
    
    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            display_filtered_logs(filtered_logs, log_level)
        else:
            print(f"No logs found")

if __name__ == "__main__":
    main()

# python3 main.py logfile.log 
