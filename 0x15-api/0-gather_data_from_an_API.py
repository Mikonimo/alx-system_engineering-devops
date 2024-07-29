#!/usr/bin/python3
"""This module gathers data from an API"""
import requests
import sys


def fetch_employee_data(employee_id):
    # Base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee data
    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch todos for the employee
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data['name']

    # Extract and count tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)

    # Print the required output
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print(f'\t {task["title"]}')


if __name__ == '__main__':
    # Ensure an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print('Usage: python3 script_name.py EMPLOYEE_ID')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('EMPLOYEE_ID must be an integer.')
        sys.exit(1)

    fetch_employee_data(employee_id)
