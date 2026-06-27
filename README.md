# Task Tracker CLI

(https://roadmap.sh/projects/task-tracker)A simple command-line task tracker built with Python.

This project allows you to add, update, delete, mark, and list tasks from the terminal. Tasks are stored locally in a JSON file named `tasks.json`.

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as in progress
* Mark tasks as done
* List all tasks
* List tasks by status:

  * `todo`
  * `in-progress`
  * `done`
* Store tasks in a local JSON file
* Automatically create `tasks.json` if it does not exist

## Requirements

* Python 3 installed
* No external libraries required

This project only uses Python built-in modules:

* `sys`
* `os`
* `json`
* `datetime`

## Project Structure

```text
Task-Tracker/
│
├── main.py
├── tasks.json
└── README.md
```

## How It Works

The app reads commands from the terminal using positional arguments.

Example:

```bash
python main.py add "Buy groceries"
```

In this command:

```text
add
```

is the action.

```text
Buy groceries
```

is the task description.

The app stores all tasks inside `tasks.json`.

Each task has the following properties:

```json
{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "2026-06-27T12:00:00",
  "updatedAt": "2026-06-27T12:00:00"
}
```

## Usage

### Add a Task

```bash
python main.py add "Buy groceries"
```

Example output:

```text
Task added successfully (ID: 1)
```

### List All Tasks

```bash
python main.py list
```

Example output:

```text
1. [todo] Buy groceries
   Created: 2026-06-27T12:00:00
   Updated: 2026-06-27T12:00:00
```

### List Tasks by Status

List todo tasks:

```bash
python main.py list todo
```

List in-progress tasks:

```bash
python main.py list in-progress
```

List done tasks:

```bash
python main.py list done
```

### Update a Task

```bash
python main.py update 1 "Buy groceries and cook dinner"
```

Example output:

```text
Task 1 updated successfully.
```

### Delete a Task

```bash
python main.py delete 1
```

Example output:

```text
Task 1 deleted successfully.
```

### Mark a Task as In Progress

```bash
python main.py mark-in-progress 1
```

Example output:

```text
Task 1 marked as in-progress.
```

### Mark a Task as Done

```bash
python main.py mark-done 1
```

Example output:

```text
Task 1 marked as done.
```

## Task Statuses

A task can have one of these statuses:

| Status        | Meaning                               |
| ------------- | ------------------------------------- |
| `todo`        | The task has not started yet          |
| `in-progress` | The task is currently being worked on |
| `done`        | The task is completed                 |

## Data Storage

Tasks are stored in `tasks.json`.

If the file does not exist, the program creates it automatically with an empty list:

```json
[]
```

The JSON file acts as a simple local database for this project.

## Example Workflow

```bash
python main.py add "Buy groceries"
python main.py add "Read Python file handling"
python main.py list
python main.py mark-in-progress 2
python main.py mark-done 1
python main.py list done
python main.py update 2 "Read Python JSON handling"
python main.py delete 1
```

## Error Handling

The app handles common user mistakes, such as:

* Missing command
* Missing task description
* Missing task ID
* Invalid status filter
* Task not found

Example:

```bash
python main.py add
```

Output:

```text
Error: Please provide a task description.
Example: python main.py add "Buy groceries"
```

## What I Learned

This project helped practice important programming concepts:

* Reading command-line arguments
* Using conditional statements
* Creating and using functions
* Reading from files
* Writing to files
* Working with JSON data
* Managing a list of dictionaries
* Handling user input errors
* Building a small CLI application

## Future Improvements

Possible improvements:

* Add better validation for task IDs
* Prevent empty task descriptions
* Add search functionality
* Add task priorities
* Add due dates
* Add a proper CLI parser using `argparse`
* Add tests
* Package the app so it can run as `task-cli`

## Author

Built as a beginner-friendly Python backend learning project.
