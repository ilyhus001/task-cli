import datetime
import os
import json

FILE = "tasks.json"

def init():
    if(os.path.exists(FILE)):
        print("exists")
    else:
        empty_tasks()  # Initialize with an empty list

def read_json() -> list[dict]:
   with open(FILE, "r") as file:
        data = json.load(file)  # Load and parse the JSON file
        return data 

def write_json(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)

def empty_tasks():
    with open(FILE, "w") as file:
        json.dump([], file)

def add(task: str):
    tasks = read_json()
    data = {
      "id": len(tasks) + 1,
      "description": task, 
      "status": "todo",
      "createdAt": datetime.datetime.now().isoformat(),
      "updatedAt": datetime.datetime.now().isoformat()
    }
    tasks.append(data)
    write_json(tasks)

def delete(id):
    tasks = read_json()
    for task in tasks:
        if task.get('id') == id:
            tasks.remove(task)
            update_ids(tasks)
            break
    write_json(tasks)

def update_ids(tasks):
    count = 1
    for task in tasks:
        task['id'] = count
        count+=1


def main():
    delete(1)
    print(read_json())
   

if __name__ == "__main__":
    main()