import csv
import requests

def get_employee_todo_progress(employee_id):
    # URL of the REST API
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    # Sending a GET request to the API
    response = requests.get(url)
    
    # Checking if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data from the API.")
        return
    
    # Extracting JSON data from the response
    todos = response.json()
    
    # Getting the employee name
    employee_name = todos[0]['username']
    
    # Counting the number of completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    
    # Total number of tasks
    total_tasks = len(todos)
    
    # Writing data to CSV file
    with open(f"employee_{employee_id}_todo_progress.csv", "w", newline="") as csvfile:
        fieldnames = ['Employee Name', 'Number of Completed Tasks', 'Total Number of Tasks']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({'Employee Name': employee_name, 'Number of Completed Tasks': num_completed_tasks, 'Total Number of Tasks': total_tasks})
        
        writer.writerow({'Task Titles': 'Completed Tasks'})
        for task in completed_tasks:
            writer.writerow({'Task Titles': task['title']})

    print(f"Data has been exported to employee_{employee_id}_todo_progress.csv")

# Example usage
employee_id = int(input("Enter the employee ID: "))
get_employee_todo_progress(employee_id)

