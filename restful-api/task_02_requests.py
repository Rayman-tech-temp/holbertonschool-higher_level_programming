#!/usr/bin/env python3
"""simple fetch and process posts script"""

import requests
import json
import csv
def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    info = r.json()
    status = r.status_code
    print("Status Code : {}".format(status))

    for key, value in info:
        if key == 'title' or key == 'body':
            print(value)

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    info = r.json()
    fn = 'posts.csv'
    indexes = []
    for key in info:
        indexes.append(key)
    with open(fn, 'w', newline=='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=indexes)
        writer.writeheader()
        writer.writerows(info)
