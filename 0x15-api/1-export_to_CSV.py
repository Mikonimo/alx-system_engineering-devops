#!/usr/bin/python3
"""Exports data to the CSV format"""
import requests
import sys
import csv


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
    employee_name = user_data['username']

    return employee_id, employee_name, todos_data


def export_to_csv(employee_id, employee_name, todos_data):
    # CSV file name
    csv_filename = f'{employee_id}.csv'

    # Write to CSV
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name,
                            task['completed'], task['title']])


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

    employee_id, employee_name, todos_data = fetch_employee_data(employee_id)
    export_to_csv(employee_id, employee_name, todos_data)
