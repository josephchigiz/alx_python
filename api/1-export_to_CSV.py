import csv
import requests
import sys

id = sys.argv[1]

request_user = requests.get('https://jsonplaceholder.typicode.com/users/'+id)
request_todos = requests.get('https://jsonplaceholder.typicode.com/users/'+id+'/todos')

data_user = request_user.json()
data_todos = request_todos.json()

completed = 0

tasks_data = []

for i in data_todos:
    if i.get('completed')==True:
        completed = completed + 1
    tasks_data.append([id, data_user.get('name'), i.get('completed'), i.get('title')])

print ('Employee {} is done with tasks({}/{}):'.format(data_user.get('name'), completed,len(data_todos)))

for item in data_todos:
    if item.get('completed') == True:
        print('\t ' + item.get('title'))

csv_file_name = f'{id}.csv'

with open(csv_file_name, mode='w', newline='') as file:
    csv_writer = csv_writer(file)
    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK TITLE"])
    csv_writer.writerows(tasks_data)
