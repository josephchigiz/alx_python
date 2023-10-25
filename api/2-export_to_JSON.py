#!/usr/bin/python
import json
import requests
#initialize empty dict
all_tasks = {}

# loop through user IDs from 1 to 10
for user_id in range(1, 11):
    # send get request to receive the TODO list for specified user
    request = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    #parse JSON data from the response
    data = request.json()

    tasks = []

    #iterate through each TODO item and structure the data
    for item in data:
        # #
        tasks.append({
            "username": f"USER_{user_id}",
            "task": item.get('title'),
            "completed": item.get('completed')
        })

    #add user's tasks to all_tasks dictionary
    all_tasks[str(user_id)] = tasks

# JSON file name
json_file = "USER_ID.json"

#open JSON file for writing
with open(json_file, mode='w') as file:
    # write collected data to JSON file
    json.dump(all_tasks, file)