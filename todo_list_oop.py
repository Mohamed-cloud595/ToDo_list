# this code i do with the help of chatgpt

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self):
        item = input("Enter the item to add: ")
        self.items.append(item)
        print(f"'{item}' added to the list.")

    def view_items(self):
        if not self.items:
            print("The list is empty.")
        else:
            print("Current list:")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")

    def remove_item(self):
        if not self.items:
            print("The list is empty.")
            return
        try:
            index = int(input("Enter the number of the item to remove: ")) - 1
            if 0 <= index < len(self.items):
                removed = self.items.pop(index)
                print(f"'{removed}' removed from the list.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

class Menu:
    def __init__(self):
        self.todo_list = TodoList()

    def display_menu(self):
        print("\nMenu:")
        print("1. Add an item")
        print("2. View the list")
        print("3. Remove an item")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option (1-4): ").strip()
            if choice == "1":
                self.todo_list.add_item()
            elif choice == "2":
                self.todo_list.view_items()
            elif choice == "3":
                self.todo_list.remove_item()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Menu().run()
