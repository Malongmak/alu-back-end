#!/usr/bin/python3
import request

BASE_URL = "https://jsonplaceholder.typicode.com/todos"

def get_todo_list_progress(employee_id):
    response = requests.get(f"{BASE_URL}/{employee_id}")

    if response.status_code == 200:
        data = response.json()

        number_of_completed_tasks = len([task for task in data if task["completed"]])

        total_number_of_tasks = len(data)

        print(f"Employee {data['name']} is done with tasks({number_of_completed_tasks}/{total_number_of_tasks}):")

        for task in data:
            if task["completed"]:
                print("\t", task["title"])

    else:
        print("Error getting TODO list progress.")

employee_id = int(input("Enter the employee ID: "))

get_todo_list_progress(employee_id)
