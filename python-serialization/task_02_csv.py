#!/usr/bin/env python3

import csv
import json
"""
functions that convert csv data into json file
"""


def convert_csv_to_json(csv_file):
    """
    this writes the binary into a JSON file
    """
    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as csvfile:
            information = list(csv.DictReader(csvfile))

        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(information, jsonfile, indent=4)

        csvfile.close()
        jsonfile.close()
        return (True)

    except IOError, EOFError:
        return (False)
