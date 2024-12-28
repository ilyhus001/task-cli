import os
import json

FILE = "tasks.json"

def init():
    if(os.path.exists(FILE)):
        print("exists")
    else:
        with open(FILE, "w") as file:
            json.dump([], file)  # Initialize with an empty list

def main():
    init()

if __name__ == "__main__":
    main()