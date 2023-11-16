import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found. Add a task using 'add'.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Task '{new_task}' added successfully.")

def remove_task(tasks, task_index):
    if task_index >= 1 and task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed successfully.")
    else:
        print("Invalid task index. Please provide a valid index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nCommands:")
        print("1. Show tasks (show)")
        print("2. Add task (add)")
        print("3. Remove task (remove)")
        print("4. Quit (quit)")

        choice = input("Enter your choice: ").lower()

        if choice == "show":
            show_tasks(tasks)
        elif choice == "add":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "remove":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == "quit":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
