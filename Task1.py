from datetime import datetime
import uuid
 
 
class Task:
    all_tasks = {}
    complete_tasks = {}
    incomplete_tasks = {}
 
    def __init__(self, id, number, task, create_time) -> None:
        self.id = id
        self.task = task
        self.create_time = create_time
        self.number = number
        self.Updated_time = "NA"
        self.Completed = False
        self.Completed_time = "NA"
        self.all_task = {"ID": id, "Task": self.task,
                         "Create time": self.create_time, "Update_time": self.Updated_time, "Completed": self.Completed, "Completed_time": self.Completed_time}
        self.all_tasks[number] = self.all_task
        self.incomplete_tasks[number] = self.all_task
 
    def update_task(self, number, task, create_time):
        self.task = task
        self.Updated_time = create_time
        self.update_tasks = self.all_tasks[number]
        self.update_tasks["Task"] = self.task
        self.update_tasks["Update_time"] = self.Updated_time
 
    def complete_task(self, number):
        self.Completed_time = new_times()
        self.Completed = False
        self.update_tasks = self.all_tasks[number]
        self.update_tasks["Completed"] = True
        self.update_tasks["Completed_time"] = self.Completed_time
        self.complete_tasks[number] = self.all_tasks[number]
        del self.incomplete_tasks[number]
 
 
def new_times():
    time = datetime.now()
    create_time = f"{time.month}/{time.day}/{time.year} {time.hour}:{time.minute}:{time.second}"
    return create_time
 
 
def task_display(all_task):
    is_ok = True
    for task in all_task:
        print()
        for key, value in all_task[task].items():
            print(f"{key} - {value}")
            is_ok = False
    print()
    if is_ok:
        return is_ok
 
 
def check(all_task):
    is_ok = True
    for task in all_task:
        for key, value in all_task[task].items():
            is_ok = False
    if is_ok:
        return is_ok
 
 
def Update_task_display(all_task):
    for task in all_task:
        print("\nTask No - ", task)
        for key, value in all_task[task].items():
            print(f"{key} - {value}")
 
 
number = 0
while (True):
    print("1. Add New Task")
    print("2. Show All Task")
    print("3. Show Incomplete Tasks")
    print("4. Show Completed Tasks")
    print("5. Update Task")
    print("6. Mark A Task Completed")
    option = int(input("Enter Option:"))
    if option == 1:
        number = number + 1
        name = input("Enter new Task: ")
        id = uuid.uuid1()
        create_time = new_times()
        People = Task(id, number, name, create_time)
        print("\nTask Created Successfully\n")
    elif option == 2:
        task_display(People.all_tasks)
    elif option == 3:
        is_ok = task_display(People.incomplete_tasks)
        if is_ok:
            print("No In-Completed Task\n")
    elif option == 4:
        is_ok = task_display(People.complete_tasks)
        if is_ok:
            print("No Completed Task\n")
    elif option == 5:
        if check(People.incomplete_tasks):
            print("\nNo Task To Update\n")
            continue
        print("\nSelect Which Task To Update\n")
        Update_task_display(People.incomplete_tasks)
        number = int(input("\nEnter Task No: "))
        task = input("Enter New Task: ")
        create_time = new_times()
        People.update_task(number, task, new_times())
        print("\nTask Updated Successfully\n")
    elif option == 6:
        if check(People.incomplete_tasks):
            print("\nNo Task To Complete\n")
            continue
        Update_task_display(People.incomplete_tasks)
        number = int(input("\nEnter Task No: "))
        People.complete_task(number)
        print("\nTask Complete Successfully\n")
    else:
        break