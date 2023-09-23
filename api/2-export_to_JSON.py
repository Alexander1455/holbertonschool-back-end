#!/usr/bin/python3
"""Python script that using REST API and export json"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response1 = requests.get(todo_url).json()
    response2 = requests.get(user_url).json()

    number_tasks_done = sum(1 for task in response1 if task["completed"])
    total_tasks = len(response1)

    employee_name = response2.get("name")
    employee_username = response2.get("username")
    employee_status = [task["completed"] for task in response1]
    all_task_titles = [task["title"] for task in response1]

    task_titles = [task["title"] for task in response1 if task["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
          employee_name, number_tasks_done, total_tasks))
    for title in task_titles:
        print(f"\t {title}")

    employee_data = {
        user_id: [
            {
                "task": all_task_titles[i],
                "completed": employee_status[i],
                "username": employee_username
            }
            for i in range(len(all_task_titles))
        ]
    }

    "Export json"
    filename_json = f"{user_id}.json"

    with open(filename_json, mode="w", newline="") as json_file:
        json.dump(employee_data, json_file)
