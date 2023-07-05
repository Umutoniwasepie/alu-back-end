#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import csv
import requests
from sys import argv

def get_user_info(user_id):
    """
    Retrieves user information based on the user ID.
    """
    user_info = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    return user_info

def get_todo_list(user_id):
    """
    Retrieves the TODO list for the specified user ID.
    """
    todo_list = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}").json()
    return todo_list

def export_to_csv(user_id):
    """
    Exports the employee's task data to a CSV file.
    """
    user_info = get_user_info(user_id)
    username = user_info.get('username')
    todo_list = get_todo_list(user_id)

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for task in todo_list:
            task_completed = str(task.get('completed'))
            task_title = task.get('title')

            writer.writerow([user_id, username, task_completed, task_title])

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: {} employee_id'.format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    export_to_csv(employee_id)
