tasks = {}

def add_task():
    task = input("Enter the task: ")
    tasks[len(tasks) + 1] = task
    print("Task added successfully!")


def delete_task():
    task_number = int(input("Enter the task number to delete: "))
    if task_number in tasks:
        del tasks[task_number]
        print("Task deleted successfully!")
    else:
        print("Task number not found!")


def display_tasks():
    if tasks:
        print("Tasks:")
        for task_number, task in tasks.items():
            print(f"{task_number}. {task}")
    else:
        print("No tasks added yet!")


def main():
    while True:
        print("\nWelcome to the To-Do List App")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            print("Thank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
