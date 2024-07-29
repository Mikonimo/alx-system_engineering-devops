#!/usr/bin/python3
""" Export data in JSON format"""
import json
import requests


def fetch_data():
    # Fetch user data
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    # Fetch todo data
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos_response.json()

    return users, todos


def main():
    users, todos = fetch_data()

    data = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        tasks = []
        for todo in todos:
            if todo['userId'] == user_id:
                task_info = {
                    'username': username,
                    'task': todo['title'],
                    'completed': todo['completed']
                }
                tasks.append(task_info)

        data[user_id] = tasks

    # Save to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
