#!/usr/bin/python3
""" Returns information about his/her TODO list progress using a API """

import requests
import sys

if __name__ == "__main__":
    empID = sys.argv[1]

    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(empID))
    resp_Todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(empID))

    obj_resp = response.json()
    obj_Todos = resp_Todos.json()

    taskDone = []
    for task in obj_Todos:
        if task['completed']:
            taskDone.append(task['title'])

    print("Employee {} is done with tasks({}/{}):"
          .format(obj_resp['name'], len(taskDone), len(obj_Todos)))
    for i in range(len(taskDone)):
        print("\t {}".format(taskDone[i]))
