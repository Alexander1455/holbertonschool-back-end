#!/usr/bin/python3
"""Python script that using REST API and export json"""
import json
import requests

if __name__ == "__main__":
    todo_url = f"https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users"

    response1 = requests.get(todo_url).json()
    response2 = requests.get(user_url).json()

    number_tasks_done = sum(1 for task in response1 if task["completed"])
    total_tasks = len(response1)

    employee_data = {}

    for user in response2:
        user_id = user["id"]
        employee_username = user["username"]
        employee_status = [task["completed"] for task in response1
                           if task["userId"] == user_id]
        task_titles = [task["title"] for task in response1
                       if task["userId"] == user_id]

        employee_data[user_id] = [
                {
                    "username": employee_username,
                    "task": title,
                    "completed": status
                }
                for title, status in zip(task_titles, employee_status)
            ]

    filename_json = "todo_all_employees.json"

    with open(filename_json, mode="w") as json_file:
        json.dump(employee_data, json_file)
