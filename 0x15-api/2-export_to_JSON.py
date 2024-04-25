#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user_re = requests.get(user_url)
    todos_re = requests.get(todos_url)

    if user_re.status_code != 200 or todos_re.status_code != 200:
        print("Failed to retrieve data from the API.")
        exit(1)

    user = user_re.json()
    todos = todos_re.json()
    username = user['username']
    all_tasks = []

    format = {f'{user_id}': [{
                                "task": f"{task['title']}",
                                "completed": f"{task['completed']}",
                                "username": f"{username}"
                             } for task in todos]}

    with open("{}.json".format(user_id), 'w+') as jsonfile:
        json.dump(format, jsonfile)


if __name__ == "__main__":
    main()
