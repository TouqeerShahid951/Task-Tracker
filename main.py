import sys
import os
import json
from datetime import datetime

FILE_NAME = "tasks.json"


def create_file_if_not_exists():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("[]")


def load_tasks():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=2)


def get_next_id(tasks):
    if len(tasks) == 0:
        return 1

    return max(task["id"] for task in tasks) + 1


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def add_task(tasks, description):
    now = datetime.now().isoformat()

    task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {task['id']})")


def list_tasks(tasks, status_filter=None):
    if status_filter is not None:
        tasks = [task for task in tasks if task["status"] == status_filter]

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"{task['id']}. [{task['status']}] {task['description']}")
        print(f"   Created: {task['createdAt']}")
        print(f"   Updated: {task['updatedAt']}")


def update_task(tasks, task_id, new_description):
    task = find_task_by_id(tasks, task_id)

    if task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return

    task["description"] = new_description
    task["updatedAt"] = datetime.now().isoformat()

    save_tasks(tasks)

    print(f"Task {task_id} updated successfully.")


def delete_task(tasks, task_id):
    task = find_task_by_id(tasks, task_id)

    if task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return

    tasks.remove(task)
    save_tasks(tasks)

    print(f"Task {task_id} deleted successfully.")


def change_task_status(tasks, task_id, new_status):
    task = find_task_by_id(tasks, task_id)

    if task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return

    task["status"] = new_status
    task["updatedAt"] = datetime.now().isoformat()

    save_tasks(tasks)

    print(f"Task {task_id} marked as {new_status}.")


def show_help():
    print("Task Tracker CLI")
    print()
    print("Usage:")
    print('  python task_cli.py add "Task description"')
    print('  python task_cli.py update <id> "New description"')
    print("  python task_cli.py delete <id>")
    print("  python task_cli.py mark-in-progress <id>")
    print("  python task_cli.py mark-done <id>")
    print("  python task_cli.py list")
    print("  python task_cli.py list todo")
    print("  python task_cli.py list in-progress")
    print("  python task_cli.py list done")


def main():
    create_file_if_not_exists()
    tasks = load_tasks()

    if len(sys.argv) < 2:
        print("Error: Please provide a command.")
        show_help()
        sys.exit()

    action = sys.argv[1]

    if action == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a task description.")
            print('Example: python task_cli.py add "Buy groceries"')
            sys.exit()

        description = sys.argv[2]
        add_task(tasks, description)

    elif action == "list":
        if len(sys.argv) == 2:
            list_tasks(tasks)

        elif len(sys.argv) == 3:
            status_filter = sys.argv[2]

            if status_filter not in ["todo", "in-progress", "done"]:
                print("Error: Invalid status filter.")
                print("Allowed filters: todo, in-progress, done")
                sys.exit()

            list_tasks(tasks, status_filter)

        else:
            print("Error: Too many arguments for list command.")
            print("Example: python task_cli.py list done")

    elif action == "update":
        if len(sys.argv) < 4:
            print("Error: Please provide task ID and new description.")
            print('Example: python task_cli.py update 1 "Buy groceries and cook dinner"')
            sys.exit()

        task_id = int(sys.argv[2])
        new_description = sys.argv[3]

        update_task(tasks, task_id, new_description)

    elif action == "delete":
        if len(sys.argv) < 3:
            print("Error: Please provide task ID.")
            print("Example: python task_cli.py delete 1")
            sys.exit()

        task_id = int(sys.argv[2])

        delete_task(tasks, task_id)

    elif action == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Please provide task ID.")
            print("Example: python task_cli.py mark-in-progress 1")
            sys.exit()

        task_id = int(sys.argv[2])

        change_task_status(tasks, task_id, "in-progress")

    elif action == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Please provide task ID.")
            print("Example: python task_cli.py mark-done 1")
            sys.exit()

        task_id = int(sys.argv[2])

        change_task_status(tasks, task_id, "done")

    else:
        print("Error: Unknown command.")
        show_help()


main()