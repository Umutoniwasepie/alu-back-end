#!/usr/bin/python3

"""
Module: gather_data_from_an_API
"""

import requests
from sys import argv


def gather_data(employee_id):
    """
    Fetches employee data from API and displays TODO list progress.
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}'
    todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'
       url = url.format(employee_id)   
       todo = todo.format(employee_id)
    
    response_user = requests.get(url_user).json()
    response_tasks = requests.get(url_tasks).json()

    employee_name = response_user.get('name')
    tasks_total = len(response_tasks)
    tasks_completed = [task for task in response_tasks if task.get('completed')]

    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name,
        len(tasks_completed),
        tasks_total
    ))

    for task in tasks_completed:
        print('\t{}'.format(task.get('title')))


if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: {} employee_id'.format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    gather_data(employee_id)

