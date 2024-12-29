import sys
from task_manager import add, delete, update, mark_in_progress, mark_done

def main():
    commands = sys.argv[1:]
    if commands[0] != 'task-cli' or len(commands) < 1:
        print("Usage: python main.py task-cli <command> [...]")
        print("    Commands: add, delete, update, list, mark-in-progress, mark-done")

    match(commands[1]):
        case "add":
            if len(commands) != 3:
                print("add takes one parameter\nE.g. task-cli add \"Buy groceries\"")
            else:
                add(commands[2])

        case "delete":
            if len(commands) != 3:
                print("delete takes one parameter\nE.g. task-cli delete 1")
            else:
                try:
                    delete(int(commands[2]))
                except ValueError:
                    print("delete takes integers only")

        case "update":
            if len(commands) != 4:
                print("update takes 2 parameters parameter\nE.g. task-cli update 1 \"Buy groceries\"")
            else:
                try:
                    update(int(commands[2]), commands[3])
                except ValueError:
                    print("First parameter must be an integer")

        case "list":
            pass

        case "mark-in-progress":
            if len(commands) != 3:
                print("mark-in-progress takes one parameter\nE.g. task-cli mark-in-progress 1")
            else:
                try:
                    mark_in_progress(int(commands[2]))
                except ValueError:
                    print("mark-in-progress takes integers only")
                
        case "mark-done":
            if len(commands) != 3:
                print("mark-done takes one parameter\nE.g. task-cli mark-done 1")
            else:
                try:
                    mark_done(int(commands[2]))
                except ValueError:
                    print("mark-done takes integers only")

        case _:
            print("Not a recognized command")
            print("    Commands: add, delete, update, list, mark-in-progress, mark-done")

if __name__ == "__main__":
    main()