#!/usr/bin/python3
"""Fetches and exports TODO list data for a given employee in JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch employee data
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch TODO list data
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Prepare data to be written in JSON format
    tasks = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks.append(task_dict)

    data_to_export = {user_id: tasks}

    # Write the data to a JSON file
    with open(f"{user_id}.json", "w") as json_file:
        json.dump(data_to_export, json_file)
