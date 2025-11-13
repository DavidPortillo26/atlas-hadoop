#!/usr/bin/env python3
import sys
import csv

def main():
    reader = csv.reader(sys.stdin)

    # Read the header first
    header = next(reader, None)
    # Optionally check header, but we don't print it
    # Expected: id,company,title,totalyearlycompensation,...

    for row in reader:
        # Defensive: skip malformed rows
        if len(row) < 4:
            continue

        _id = row[0].strip()
        company = row[1].strip()
        total_comp = row[3].strip()  # totalyearlycompensation

        # Skip if any of the required fields are missing
        if not (_id and company and total_comp):
            continue

        # id <TAB> company,totalyearlycompensation
        print(f"{_id}\t{company},{total_comp}")

if __name__ == "__main__":
    main()
