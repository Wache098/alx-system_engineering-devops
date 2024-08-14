#!/usr/bin/python3
"""
For a given employee ID, exports information about their TODO list progress
to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(user_url).json()
    username = user.get('username')

    if not username:
        print("Employee not found.")
        sys.exit(1)

    # Fetch TODO list for the user
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todos = requests.get(todos_url).json()

    # Write to CSV file
    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get('completed'), task.get('title')])
