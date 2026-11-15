tasks=[]

def add_task():
    task_name=input("enter your task: ")

    task={
        "name" :task_name,
        "completed":False
    }

    tasks.append(task)
    print("Task added susccessfully!")

def view_task():
    if len(tasks)==0:
        print("no task added!")
    else:
        print("==========your task==========")

        for index, task in enumerate(tasks,start=1):

            if task["completed"]==True:
                status="Completed!!"
            else:
                status="Pending"

            print(f"{index}.{task['name']}-{status}")            

def delete_task():
    view_task()

    if len(tasks)==0:
       return

    task_number=int(input("Enter task number to delete: "))

    if 1<=task_number<=len(tasks):
        removed_task= tasks.pop(task_number-1)
        print(removed_task["name"],"deleted succsessfully")

    else:
         print("invalid task number!")

def complete_task():
    view_task()

    if len(tasks)==0:
       return
     
    task_number=int(input("Enter task number to complete:" ))

    if 1<=task_number<=len(tasks):

        tasks[task_number-1]["completed"]=True

        print("Task marked as completed!")

    else:
         print("invalid task number!")                    
 

while True:
    print("========== My to do list ==========")
    print("1. Add task")
    print("2. view task")
    print("3. Delete task")
    print("4. Mark task as completed")
    print("5.exit")


    choice=input("choose an option: ")

    if choice=="1":
        add_task()

    elif choice=="2":
        view_task()

    elif choice=="3":
        delete_task() 

    elif choice=="4":
        complete_task()

    elif choice=="5":
         print("Thank for using to do list!")    
         break  

    else:
        print("invalid choice!")
                          

