tasks = []

while True:
    print("\nTo-Do List:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
    elif choice == "2":
        print("\nYour tasks:")
        for task in tasks:
            print(f"- {task}")
    elif choice == "3":
        task_to_remove = input("Enter task to remove: ")
        if task_to_remove in tasks:
            tasks.remove(task_to_remove)
            print(f"'{task_to_remove}' removed from the list.")
        else:
            print("Task not found.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
