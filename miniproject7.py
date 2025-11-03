tasks = []
while True:
    print("\n--- Command-Line Task Manager ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '4':
        print("Exiting the task manager. Goodbye!")
        break
    if choice=='1':
        title=input("enter a task:")
        tasks.append({"title":title,"completed":False})
        print(f"task {title} added successfully")
    elif choice =='2':
        if not tasks:
            print("no tasks in your list")
        else:
             for i, task in enumerate(tasks, 1):
                status = "✓" if task["completed"] else " "
                print(f"{i}. [{status}] {task['title']}")
    elif choice == '3':
        if not tasks:
            print("There are no tasks to mark.")
            continue
        print("\nTasks to mark as complete:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']}")
        
        try:
            task_number = int(input("Enter the number of the task to complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

            

            
                
            
    
                       
