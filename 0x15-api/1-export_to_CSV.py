#!/usr/bin/python3
"""Export to CSV"""
import csv
import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        exit(1)

    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = user_url + "/todos"

    user_re = requests.get(user_url)
    todos_re = requests.get(todos_url)
    user = user_re.json()
    todos = todos_re.json()

    username = user['username']

    with open(f"{user_id}.csv", 'w', newline="") as file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        for task in todos:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_STATUS": task['completed'],
                "TASK_TITLE": task['title']
            })


if __name__ == "__main__":
    main()
