#!/usr/bin/python3

"""
Module: gather_data_from_an_API
"""

import requests
import sys


def get_name(employee_id):
    """
    Gets the user name based on the employee ID.
    """
    payload = {'id': employee_id}
    response = requests.get('https://jsonplaceholder.typicode.com/users', params=payload)
    user_data = response.json()
    return user_data[0]['name']


def get_task(employee_id):
    """
    Retrieves task numbers and completed todos.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_list = []
    tasks_todo = 0
    tasks_done = 0
    data = response.json()

    for item in data:
        if item['userId'] == employee_id:
            tasks_todo += 1
            if item['completed']:
                todo_list.append(item['title'])
                tasks_done += 1

    employee_name = get_name(employee_id)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        tasks_done,
        tasks_todo
    ))

    for todo in todo_list:
        print("\t{}".format(todo))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_task(employee_id)
