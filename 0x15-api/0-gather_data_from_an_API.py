#!/usr/bin/python3
"""
This script fetches data from a REST API for a given employee ID
and displays the employee's TODO list progress.
"""
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetches employee data from the API"""
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url_user)
    return response.json()


def fetch_todo_list(employee_id):
    """Fetches the TODO list for a given employee from the API"""
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url_todos)
    return response.json()


def display_todo_progress(employee_name, todos):
    """Displays the employee's TODO list progress"""
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data = fetch_employee_data(employee_id)
    employee_name = employee_data.get("name")

    if employee_name:
        todos = fetch_todo_list(employee_id)
        display_todo_progress(employee_name, todos)
    else:
        print("Employee not found.")
