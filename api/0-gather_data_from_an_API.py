#!/usr/bin/python3
"""
Script to retrieve and display information about an employee's TODO list progress
using a REST API.

Usage:
    python3 0-gather_data_from_an_API.py employee_id

Parameters:
    employee_id (int): The ID of the employee for whom to retrieve TODO list information.
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    API_URL = "https://jsonplaceholder.typicode.com"
    
    # Make a request to the API to retrieve TODO list data for the employee
    response = requests.get(
        f"{API_URL}/users/{employee_id}/todos",
        params={"_expand": "user"}
    )
    data = response.json()

    # Check if the response data is empty
    if not data:
        print(f"RequestError: No data found for employee ID {employee_id}")
        sys.exit(1)

    # Extract information from the response data
    employee_name = data[0]["user"]["name"]
    total_tasks = len(data)
    done_tasks = [task for task in data if task["completed"]]
    total_done_tasks = len(done_tasks)

    # Display information about the employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks"
          f"({total_done_tasks}/{total_tasks}):")
    
    # Display titles of completed tasks
    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("UsageError: python3 script_name.py employee_id(int)")
        sys.exit(1)

    # Retrieve employee ID from command-line argument
    employee_id = int(sys.argv[1])
    
    # Call the function to fetch and display employee TODO progress
    fetch_employee_todo_progress(employee_id)
