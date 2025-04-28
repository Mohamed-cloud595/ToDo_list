todo_list = []

while (True):
    
    user_action = input("Enter your command (add , view , remove , exit): ")
    
    if (user_action == "add"):
        task = input("Enter your task: ")
        todo_list.append(task)
        print("Task added successfully")
    
    elif (user_action == "view"):
        if not todo_list:
            print("No task available")
        else:
            print("Your tasks are:")
            for task in todo_list:
                print(task)
    
    elif (user_action == "remove"):
        if not todo_list:
            print("No task to remove ")
        else:
            task = input("Enter task to remove: ")
            if task in todo_list:
                todo_list.remove(task)
                print("Task removed successfully")
            else:
                print("Task not found")
    
    elif (user_action == "exit"):
        break
    else:
        print("Invalid command")