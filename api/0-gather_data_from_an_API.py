#!/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
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

# Prompt for employee ID
employee_id = int(input("Enter employee ID: "))

# Call the function to get employee's TODO list progress
get_employee_todo_progress(employee_id)

