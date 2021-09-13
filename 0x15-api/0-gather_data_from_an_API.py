#!/usr/bin/python3
""" Returns information about his/her TODO list progress using a API """

import requests
import sys

empID = sys.argv[1]

response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(empID))
resp_Todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(empID))

obj_resp = response.json()
obj_Todos = resp_Todos.json()


numbTask = 0
numbTaskDone = 0
taskDone = ""
for task in obj_Todos:
    if task['completed']:
        numbTaskDone += 1
        taskDone += "\t " + task['title'] + "\n"
    numbTask += 1

print("Employee {} is done with tasks ({}/{}):".format(obj_resp['name'],
      numbTaskDone, numbTask))
print(taskDone[:-1])
