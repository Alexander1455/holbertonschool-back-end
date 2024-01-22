#!/usr/bin/python3
""" This module defines the REST API """
import requests
import sys

if __name__ == "__main__":
    # Define the base URL for the REST API
    url = "https://jsonplaceholder.typicode.com"

    # Retrieve user data from the API using a user ID provided as a
    # command-line argument
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()

    # Retrieve a list of todos for the user using their user ID as a filter
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()

    # Calculate the total number of tasks and completed tasks
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo["completed"])

    # Print a summary of the user's tasks
    print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), completed_tasks, total_tasks))

    # Print the titles of completed tasks
    [print(f"\t {todo['title']}") for todo in todos if todo["completed"]]