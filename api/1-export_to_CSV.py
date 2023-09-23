#!/usr/bin/python3
"""Python script export CSV"""
import csv
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

    employee_id = response2.get("id")
    employee_username = response2.get("username")
    employee_name = response2.get("name")
    task_titles = [task["title"] for task in response1 if task["completed"]]
    all_task_titles = [task["title"] for task in response1]
    employee_status = [task["completed"] for task in response1]

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          number_tasks_done, total_tasks))
    for title in task_titles:
        print(f"\t {title}")

    "Export csv"
    filename_csv = f"{user_id}.csv"

    with open(filename_csv, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for i in range(len(all_task_titles)):
            csv_writer.writerow([employee_id, employee_username,
                                 employee_status[i], all_task_titles[i]])
