#!/usr/bin/python3
"""Gather data from
an API
"""
import requests
import sys
import json

em_id = sys.argv[1]
url_1 = f"https://jsonplaceholder.typicode.com/users/{em_id}"
url_2 = f"https://jsonplaceholder.typicode.com/users/{em_id}/todos"
user = requests.get(url_1)
todo = requests.get(url_2)

employee = user.json()
todos = todo.json()

em_name = employee["name"]
total_tasks = len(todos)
tasks = []

for task in todos:
    if task["completed"] is True:
        tasks.append(task["title"])
done_tasks = len(tasks)

print(f"Employee {em_name} is done with tasks({done_tasks}/{total_tasks}):")
for task in tasks:
    print(f"\t{task}")
