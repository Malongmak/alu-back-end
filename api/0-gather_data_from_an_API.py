#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress using a REST API.

Usage:
    python3 script_name.py employee_id

Arguments:
    employee_id (int): The ID of the employee to fetch TODO list progress for.

Example:
    python3 script_name.py 123
"""

import requests

def get_employee_todo_progress(employee_id):
    """
    Fetches the TODO list progress for the given employee ID and displays it on the standard output.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Make a GET request to the API
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    # Check if the request was successful
    if response.status_code == 200:
        todos = response.json()

        # Filter completed tasks
        completed_tasks = [todo for todo in todos if todo['completed']]

        # Get employee name
        employee_name = todos[0]['name'] if todos else 'Unknown Employee'

        # Display progress information
        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{len(todos)}):")

        # Display completed task titles
        for task in completed_tasks:
            print("\t", task['title'])
    else:
        print("Failed to retrieve TODO list.")

if __name__ == '__main__':
    import sys

    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    # Get the employee ID from the command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to get employee's TODO list progress
    get_employee_todo_progress(employee_id)

