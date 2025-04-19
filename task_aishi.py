tasks = [] 

def menu():
    print("\nTO DO LIST !\n\n")
    print("Choose from the following options \n")
    print("1. View")
    print("2. Add")
    print("3. Mark as done!")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter the choice (1 | 2 | 3 | 4): \n")

    if choice == "1":
        if not tasks:
            print("\nNo tasks for now!!")
        else:
            for i, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{i + 1}. {task['title']} - {status}")

    elif choice == "2":
        title = input("Enter your task: ")
        tasks.append({"title": title, "done": False})
        print("Task added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark as done.")
            continue
        try:
            num = int(input("Enter the task number to mark it as done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you!!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
