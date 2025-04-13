todo_list = []

# Show menu options
def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

# View all tasks
def view_tasks():
    if len(todo_list) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i in range(len(todo_list)):
            task = todo_list[i]
            status = "Done" if task["done"] else "Not Done"
            print(f"{i + 1}. {task['text']} - [{status}]")

# Add a new task
def add_task():
    task_text = input("Enter the task: ")
    new_task = {"text": task_text, "done": False}
    todo_list.append(new_task)
    print("Task added!")

# Mark a task as done
def mark_task_done():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_number < len(todo_list):
            todo_list[task_number]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

# Delete a task
def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(todo_list):
            deleted_task = todo_list.pop(task_number)
            print(f"Deleted: {deleted_task['text']}")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

# Run the main app loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thanks for using the To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
