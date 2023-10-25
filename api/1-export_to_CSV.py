#usr/bin/python
import csv
import requests
import sys

id = sys.argv[1]
request_user = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
request_todos = requests.get('https://jsonplaceholder.typicode.com/users/' + id + '/todos')
data_user = request_user.json()
data_todos = request_todos.json()
completed = 0
tasks = []

for i in data_todos:
    if i.get('completed') == True:
        completed = completed + 1
        tasks.append([id, data_user.get('name'), "Completed", i.get('title')])
    else:
        tasks.append([id, data_user.get('name'), "Not Completed", i.get('title')])

csv_file = "{}.csv".format(id)

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    #columns
    writer.writerows(tasks)

print(f'Employee {data_user.get("name")} is done with tasks ({completed}/{len(data_todos)}):')
for item in data_todos:
    if item.get('completed') == True:
        print(f'\t {item.get("title")}')

print(f'Data exported to {csv_file}.')