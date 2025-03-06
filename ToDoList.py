# Simple To-Do List Program

def show_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = []
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"'{task}' added!")

        elif choice == '2':
            show_tasks(tasks)
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"'{removed_task}' removed!")
            else:
                print("Invalid task number!")

        elif choice == '3':
            show_tasks(tasks)

        elif choice == '4':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()