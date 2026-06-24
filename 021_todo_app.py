"""
Simple Todo App
Add, view, mark complete, and delete tasks.
"""

# list to store tasks
tasks = []


def show_tasks():
    """Show all tasks."""
    if not tasks:
        print("\n📭 Your todo list is empty!")
        return
    
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}) {status} {task['name']}")


def add_task(name):
    """Add a new task."""
    new_task = {
        "name": name,
        "done": False
    }
    tasks.append(new_task)
    print(f"✅ Added: {name}")


def mark_complete(task_number):
    """Mark a task as complete."""
    try:
        index = task_number - 1
        if index < 0 or index >= len(tasks):
            print("❌ Invalid task number!")
            return
        
        tasks[index]["done"] = True
        print(f"✅ Marked complete: {tasks[index]['name']}")
    except ValueError:
        print("❌ Please enter a valid number!")


def delete_task(task_number):
    """Delete a task."""
    try:
        index = task_number - 1
        if index < 0 or index >= len(tasks):
            print("❌ Invalid task number!")
            return
        
        deleted = tasks.pop(index)
        print(f"🗑️ Deleted: {deleted['name']}")
    except ValueError:
        print("❌ Please enter a valid number!")


def main():
    print("📝 Welcome to Todo App!")
    print("=" * 40)
    
    while True:
        show_tasks()
        
        print("\nWhat do you want to do?")
        print("1) Add a task")
        print("2) Mark task as complete")
        print("3) Delete a task")
        print("4) Quit")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "1":
            task_name = input("Enter task name: ").strip()
            if task_name:
                add_task(task_name)
            else:
                print("❌ Task name cannot be empty!")
        
        elif choice == "2":
            if tasks:
                try:
                    task_num = int(input("Enter task number to mark complete: "))
                    mark_complete(task_num)
                except ValueError:
                    print("❌ Please enter a valid number!")
            else:
                print("❌ No tasks to mark complete!")
        
        elif choice == "3":
            if tasks:
                try:
                    task_num = int(input("Enter task number to delete: "))
                    delete_task(task_num)
                except ValueError:
                    print("❌ Please enter a valid number!")
            else:
                print("❌ No tasks to delete!")
        
        elif choice == "4":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Try again.")


main()
