#!/usr/bin/env python3
import sys

TOP_N = 10


def main():
    top_entries = []  # holds at most TOP_N entries

    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue

        try:
            _id, value = line.split("\t", 1)
        except ValueError:
            continue

        _id = _id.strip()

        try:
            company, total_str = value.split(",", 1)
        except ValueError:
            continue

        company = company.strip()
        total_str = total_str.strip()

        if not (_id and company and total_str):
            continue

        try:
            total = float(total_str)
        except ValueError:
            continue

        top_entries.append((total, _id, company, total_str))
        top_entries.sort(key=lambda entry: entry[0], reverse=True)

        if len(top_entries) > TOP_N:
            top_entries.pop()

    if top_entries:
        print("id\tSalary\tcompany")
        for total, _id, company, total_str in top_entries:
            # total_str preserves original formatting (e.g., trailing .0)
            print(f"{_id}\t{total_str}\t{company}")


if __name__ == "__main__":
    main()
