import datetime
import os
import json

FILE = "tasks.json"

def init() -> None:
    if(os.path.exists(FILE)):
        print("exists")
    else:
        empty_tasks()  # Initialize with an empty list

def read_json() -> list[dict]:
   with open(FILE, "r") as file:
        data = json.load(file)  # Load and parse the JSON file
        return data 

def write_json(data: list[dict]) -> None:
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)

def empty_tasks() -> None:
    with open(FILE, "w") as file:
        json.dump([], file)

def update_ids(tasks: list[dict]) -> None:
    count = 1
    for task in tasks:
        task['id'] = count
        count+=1

def add(task: str) -> None:
    tasks = read_json()
    data = {
      "id": len(tasks) + 1,
      "description": task, 
      "status": "todo",
      "createdAt": datetime.datetime.now().isoformat(),
      "updatedAt": datetime.datetime.now().isoformat()
    }
    tasks.append(data)
    print(f"Task added successfully (ID: {len(tasks)})")
    write_json(tasks)

def delete(id: int) -> None:
    tasks = read_json()
    for task in tasks:
        if task.get('id') == id:
            tasks.remove(task)
            update_ids(tasks)
            break
    write_json(tasks)

def update(id: int, new_description: str) -> None:
    tasks = read_json()
    for task in tasks:
        if task.get('id') == id:
            task['description'] = new_description
            task['updatedAt'] = datetime.datetime.now().isoformat()
            break
    write_json(tasks)

def mark_in_progress(id: int) -> None:
    tasks = read_json()
    for task in tasks:
        if task.get('id') == id:
            task['status'] = "in-progress"
            task['updatedAt'] = datetime.datetime.now().isoformat()
            break
    write_json(tasks)

def mark_done(id: int) -> None:
    tasks = read_json()
    for task in tasks:
        if task.get('id') == id:
            task['status'] = "done"
            task['updatedAt'] = datetime.datetime.now().isoformat()
            break
    write_json(tasks)

def main():
    update(3, "test")
    mark_done(3)
    print(read_json())
   

if __name__ == "__main__":
    main()