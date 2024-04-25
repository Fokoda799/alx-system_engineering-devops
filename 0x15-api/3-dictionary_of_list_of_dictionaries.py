#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests
import sys

if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    tasks = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    all_users = {}

    for user in users:
        all_tasks = []
        for task in tasks:
            if (task.get("userId") == user.get('id')):
                temp = {}
                temp["task"] = task.get("title")
                temp["completed"] = task.get("completed")
                temp["username"] = user.get("username")
                all_tasks.append(temp)
        all_users[user['id']] = all_tasks

    with open("todo_all_employees.json", 'w+') as jsonfile:
        json.dump(all_users, jsonfile, indent=4)
