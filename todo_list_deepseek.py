import json
import os
from datetime import datetime

TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from a JSON file if it exists."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Add a new task with additional metadata."""
    task_description = input("Enter your task: ").strip()
    if not task_description:
        print("Task description cannot be empty!")
        return
    
    task = {
        'id': len(tasks) + 1,
        'description': task_description,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'completed': False,
        'priority': input("Enter priority (high/medium/low): ").lower() or 'medium',
        'category': input("Enter category (optional): ").strip() or 'general'
    }
    
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task_description}' added successfully with ID {task['id']}")

def view_tasks(tasks, filter_completed=None, category=None):
    """Display tasks with filtering options."""
    if not tasks:
        print("No tasks available.")
        return
    
    filtered_tasks = tasks
    
    if filter_completed is not None:
        filtered_tasks = [t for t in filtered_tasks if t['completed'] == filter_completed]
    
    if category:
        filtered_tasks = [t for t in filtered_tasks if t['category'].lower() == category.lower()]
    
    if not filtered_tasks:
        print("No tasks match your criteria.")
        return
    
    print("\nYour tasks:")
    print("-" * 50)
    for task in filtered_tasks:
        status = "✓" if task['completed'] else " "
        print(f"{task['id']}. [{status}] {task['description']}")
        print(f"   Priority: {task['priority'].upper()}, Category: {task['category']}")
        print(f"   Created: {task['created_at']}")
        print("-" * 50)

def remove_task(tasks):
    """Remove a task by ID or description."""
    if not tasks:
        print("No tasks to remove.")
        return
    
    view_tasks(tasks)
    identifier = input("Enter task ID or description to remove: ").strip()
    
    try:
        # Try to remove by ID first
        task_id = int(identifier)
        for task in tasks:
            if task['id'] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print(f"Task ID {task_id} removed successfully.")
                return
        print(f"No task found with ID {task_id}.")
    except ValueError:
        # If not an ID, try to remove by description
        removed = False
        for task in tasks[:]:  # Create a copy for iteration
            if task['description'].lower() == identifier.lower():
                tasks.remove(task)
                removed = True
        
        if removed:
            save_tasks(tasks)
            print(f"Task '{identifier}' removed successfully.")
        else:
            print(f"No task found with description '{identifier}'.")

def complete_task(tasks):
    """Mark a task as completed."""
    if not tasks:
        print("No tasks available.")
        return
    
    view_tasks(tasks, filter_completed=False)
    try:
        task_id = int(input("Enter task ID to mark as complete: "))
        for task in tasks:
            if task['id'] == task_id:
                if task['completed']:
                    print("Task is already completed.")
                else:
                    task['completed'] = True
                    task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    save_tasks(tasks)
                    print(f"Task ID {task_id} marked as complete.")
                return
        print(f"No task found with ID {task_id}.")
    except ValueError:
        print("Please enter a valid task ID.")

def edit_task(tasks):
    """Edit an existing task."""
    if not tasks:
        print("No tasks available to edit.")
        return
    
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to edit: "))
        for task in tasks:
            if task['id'] == task_id:
                print(f"\nEditing Task ID {task_id}:")
                print(f"Current description: {task['description']}")
                new_description = input("Enter new description (leave blank to keep current): ").strip()
                if new_description:
                    task['description'] = new_description
                
                print(f"Current priority: {task['priority']}")
                new_priority = input("Enter new priority (high/medium/low, leave blank to keep current): ").strip().lower()
                if new_priority in ['high', 'medium', 'low']:
                    task['priority'] = new_priority
                
                print(f"Current category: {task['category']}")
                new_category = input("Enter new category (leave blank to keep current): ").strip()
                if new_category:
                    task['category'] = new_category
                
                save_tasks(tasks)
                print("Task updated successfully.")
                return
        print(f"No task found with ID {task_id}.")
    except ValueError:
        print("Please enter a valid task ID.")

def display_menu():
    """Display the application menu."""
    print("\n" + "=" * 30)
    print(" TO-DO LIST APPLICATION")
    print("=" * 30)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. View Completed Tasks")
    print("5. Mark Task as Complete")
    print("6. Edit Task")
    print("7. Remove Task")
    print("8. View Tasks by Category")
    print("9. Exit")
    print("=" * 30)

def main():
    """Main application loop."""
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks, filter_completed=False)
        elif choice == '4':
            view_tasks(tasks, filter_completed=True)
        elif choice == '5':
            complete_task(tasks)
        elif choice == '6':
            edit_task(tasks)
        elif choice == '7':
            remove_task(tasks)
        elif choice == '8':
            category = input("Enter category to filter by: ").strip()
            view_tasks(tasks, category=category)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()