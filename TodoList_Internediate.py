tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Task '[task] added.")

def view_tasks():
    if not tasks:
        print("No taks in the list")
        return
    for index, task in enumerate(task):
            printf(f"(ibdex + 1). (task)")

def delete_task(task_number:

    try
        index = int(task_number)-1
        deleted_task = tasks.pop(index)
    print(f"Task '{deleted_task } deleted.")
    escept IndexError,ValueError):
        print("Invalid task number")
def main():
        while true;
        print("\n Optiohs")
        print(" 1. Add task")
        print("2. View Task")
        print("3. Delete task")

        choice = input("Enter the choice")

    if choice == '1 ':
           task = input("Enter task description")
           add_task(task)
    elif choice =="2":
            view_tasks()
    elif choice=="3":
            task_number = input("Enter the task number to delete")
            dalete_task(task_number)
    elif choice ==4"):
        break
    else
            print("Invalid choice")
 if __name == "__main__:
        while true:
        
