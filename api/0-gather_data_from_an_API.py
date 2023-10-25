import requests
import sys

def employee_todo_progress(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Could not get employee information.")
        return
    
    user_data = user_response.json()
    employee_name = user_data["name"]
    
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Could not get the employee's TODO list.")
        return
    
    todos_data = todos_response.json()
    
    completed_tasks = [todo for todo in todos_data if todo["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)
    
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t{task['title']}")
        
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_todo_progress(employee_id)
    