#!/usr/bin/python3
"""Python script that uses a REST API"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response1 = requests.get(todo_url)
    response2 = requests.get(user_url)

    if response1.status_code != 200 or response2.status_code != 200:
        print("Error: Unable to retrieve data.")
        sys.exit(1)

    todos = response1.json()
    user_info = response2.json()

    number_tasks_done = sum(1 for task in todos if task["completed"])
    total_tasks = len(todos)

    employee_name = user_info.get("name")
    task_titles = [task["title"] for task in todos if task["completed"]]

    print("Employee {} is done with tasks ({}/{})".format(
        employee_name, number_tasks_done, total_tasks))
    
    if task_titles:
        print("Completed tasks:")
        for title in task_titles:
            print(f"  - {title}")
    else:
        print("No completed tasks.")
