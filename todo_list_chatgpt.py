todo_list = []

def add_task(todo_list):
    task = input("Enter your task: ")
    todo_list.append(task)
    print("Task added successfully")

def view_tasks(todo_list):
    if not todo_list:
        print("No task available")
    else:
        print("Your tasks are:")
        for task in todo_list:
            print(task)

def remove_task(todo_list):
    if not todo_list:
        print("No task to remove")
    else:
        task = input("Enter task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
            print("Task removed successfully")
        else:
            print("Task not found")

def main():
    while True:
        user_action = input("Enter your command (add, view, remove, exit): ").strip().lower()
        
        if user_action == "add":
            add_task(todo_list)
        elif user_action == "view":
            view_tasks(todo_list)
        elif user_action == "remove":
            remove_task(todo_list)
        elif user_action == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()



