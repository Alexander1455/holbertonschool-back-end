#!/usr/bin/python3
"""
Script to retrieve and display information about an employee's TODO list progress
using a REST API.

Usage:
    python3 script_name.py employee_id

Parameters:
    employee_id (int): The ID of the employee for whom to retrieve TODO list information.

Example:
    python3 0-gather_data_from_an_API.py 1
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    response = requests.get(
        f"{API_URL}/users/{EMPLOYEE_ID}/todos",
        params={"_expand": "user"}
    )
    data = response.json()

    if not len(data):
        print("RequestError:", 404)
        sys.exit(1)

    employee_name = data[0]["user"]["name"]
    total_tasks = len(data)
    done_tasks = [task for task in data if task["completed"]]
    total_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({total_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")