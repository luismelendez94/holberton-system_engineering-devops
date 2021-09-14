#!/usr/bin/python3
""" Extend last Python script to export data in the CSV format """

import json
import requests
import sys

if __name__ == "__main__":
    empID = sys.argv[1]

    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(empID))
    resp_Todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(empID))

    employee = response.json()['username']
    obj_Todos = resp_Todos.json()

    empList = []
    empTask = {}

    with open("{}.json".format(empID), 'w') as json_file:
        for task in obj_Todos:
            empTask = {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": employee}
            empList.append(empTask)
        emp_dict = {empID: empList}
        json.dump(emp_dict, json_file)
