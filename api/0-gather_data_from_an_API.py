#!/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"
    
    # Retrieve employee information
    response = requests.get(employee_url)
    if response.status_code != 200:
        print(f"Error: Could not retrieve employee information for ID {employee_id}")
        return
    
    employee_data = response.json()
    employee_name = employee_data.get("name")
    
    # Retrieve TODO list information
    response = requests.get(todo_url)
    if response.status_code != 200:
        print(f"Error: Could not retrieve TODO list for employee ID {employee_id}")
        return
    
    todo_data = response.json()
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task.get("completed")]
    num_done_tasks = len(done_tasks)
    
    # Print the progress information
    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
    
    for task in done_tasks:
        print(f"\t{task.get('title')}")

# Example usage
employee_id = 1
get_employee_todo_progress(employee_id)
