#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys


def fetch_employee_data(employee_id):
    # Base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee data
    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f'Employee with ID {employee_id} not found.')
        sys.exit(1)

    user_data = user_response.json()

    # Fetch todos for the employee
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data['username']

    return employee_id, employee_name, todos_data


def display_todo_list_progress(employee_name, todos_data):
    # Extract and count tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)

    # Print the required output
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print(f'\t {task["title"]}')


def export_to_csv(employee_id, employee_name, todos_data):
    # CSV file name
    csv_filename = f'{employee_id}.csv'

    # Write to CSV
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name,
                            task['completed'], task['title']])


def export_to_json(employee_id, employee_name, todos_data):
    # JSON file name
    json_filename = f'{employee_id}.json'

    # Prepare the data
    tasks_data = [{"task": task["title"], "completed": task["completed"],
                   "username": employee_name} for task in todos_data]
    data = {str(employee_id): tasks_data}

    # Write to JSON
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file)


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
    display_todo_list_progress(employee_name, todos_data)
    export_to_csv(employee_id, employee_name, todos_data)
    export_to_json(employee_id, employee_name, todos_data)
