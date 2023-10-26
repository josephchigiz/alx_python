#!/usr/bin/python3
"""import json, requests and sys"""
import json
import requests
import sys

"""check for user ID from command given"""
user_id = str(sys.argv[1])

"""
initialize empty dict
"""
all_tasks = {}

"""loop through user IDs from 1 to 10"""
for user_id in range(1, 11):
    """send get request to receive the TODO list for specified user"""
    request = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    """parse JSON data from the response"""
    data = request.json()

    """Initialize an empty list to store tasks for this"""
    tasks = []

    """iterate through each TODO item and structure the data"""
    for item in data:
        """Append a dictionary task information to the task lists"""
        tasks.append({
            "username": f"USER_{user_id}",
            "task": item.get('title'),
            "completed": item.get('completed')
        })

    """add user's tasks to all_tasks dictionary"""
    all_tasks[str(user_id)] = tasks

"""JSON file name"""
json_file = f'{user_id}.json'

"""open JSON file for writing"""
with open(json_file, mode='w') as file:
    """write collected data to JSON file"""
    json.dump(all_tasks, file)