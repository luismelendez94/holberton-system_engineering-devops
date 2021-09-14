#!/usr/bin/python3
""" Extend last Python script to export data in the JSON format """

import json
import requests
import sys

if __name__ == "__main__":

    todosDict = {}
    employees = requests.get(
            "https://jsonplaceholder.typicode.com/users").json()

    for emp in employees:
        empID = emp['id']
        username = emp['username']

        tasks = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}"
                .format(empID)).json()

        empTasks = []
        for task in tasks:
            task = {"username": username, "task": task['title'],
                    "completed": task['completed']}
            empTasks.append(task)

        todosDict[empID] = empTasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todosDict, json_file)
