#!/usr/bin/python3
"""Export to CSV"""
import csv
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

    for task in todos:
        temp = []
        temp.extend((user_id,
                     username,
                     task.get("completed"),
                     task.get("title")))
        all_tasks.append(temp)

    with open("{}.csv".format(user_id), 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all_tasks)


if __name__ == "__main__":
    main()
