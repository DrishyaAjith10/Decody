"""
export.py

Handles exporting structured data to CSV
"""

import csv
from io import StringIO


def convert_to_csv(data):
    """
    Convert list of dicts to CSV string
    """

    output = StringIO()
    writer = csv.writer(output)

    # header
    writer.writerow(["Who", "What", "When"])

    # rows
    for item in data:
        writer.writerow([
            item.get("who"),
            item.get("what"),
            item.get("when")
        ])

    return output.getvalue()