#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):

    '''Convert a CSV file to JSON format.

    Args:
    csv_filename (str): The path to the CSV file.

    Returns:
    bool: True if the conversion was successful, False otherwise.'''

    try:
        # Read CSV data
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Serialize to JSON
        json_data = json.dumps(data, indent=4)

        # Write to data.json
        with open('data.json', 'w') as json_file:
            json_file.write(json_data)

        return True
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return False
