#!/usr/bin/python3
import json
import requests


def fetch_and_format_data():
    """Fetch users and tasks from the API and format them into a dictionary."""
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    tasks_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    users = users_response.json()
    tasks = tasks_response.json()

    all_data = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [
            {"username": username, "task": task['title'], "completed": task['completed']}
            for task in tasks if task['userId'] == user_id
        ]
        all_data[user_id] = user_tasks

    return all_data


def save_to_file(data, filename="todo_all_employees.json"):
    """Save the formatted data to a JSON file."""
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


def main():
    """Main entry point of the script."""
    data = fetch_and_format_data()
    save_to_file(data)


if __name__ == "__main__":
    main()
