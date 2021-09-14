#!/usr/bin/python3
""" Extend last Python script to export data in the CSV format """

import csv
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

    with open("{}.csv".format(empID), 'w') as csv_file:
        for task in obj_Todos:
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                           empID, employee, task['completed'], task['title']))
