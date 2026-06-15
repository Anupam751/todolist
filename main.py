# First create a virtual environment.
# For creating a virtual environment, you need to create your project folder and then open terminal and enter
#  python -m venv venv
# venv\Scripts\activate

# current objective is to, 
# load the txt as we run
# if data does not exists inside txt, create an empty list
# if data exists, add, remove or view
# save back the updated data to tasks

import json
from datetime import date
from datetime import datetime

# -----------------
#STARTING THE CODE
# -----------------

#READING TEXT FILE --------
class TASKMANAGER:
    def __init__(self):
        self.tasks = []
        try:
            with open("tasks.json","r", encoding="utf-8") as f: # r is used to read file
                self.tasks = json.load(f) # splitlines is used because the data will be in a new line in text file
            print("txt read successfully")
        except:
            print("sheet is empty")
        

#----------------READING TEXT FILE COMPLETED

#FUNCTIONS--------------
    def addTask(self):
        title = input("Enter task: ")
        dueDate = input("Enter date in (YYYY-MM-DD): ")
        while True:
            priority = input("Enter priority (high/medium/low): ").lower()
            if priority in ["high", "medium", "low"]:
                break
            else:
                print("Invalid input. Please enter high, medium, or low.")
        for task in self.tasks:
            if task["title"] == title:
                print("task already exists")
                return 
        currentDate = date.today().strftime("%Y-%m-%d")
        self.tasks.append({"title": title, "done": False, "due": dueDate, "priority": priority, "updated at": currentDate}) # example format : [{"title": "Learn Python", "done": False}]
        print("new task added")

    def delTask(self):
        if not self.tasks:
            print("no tasks to delete") 
        else:
            delete = int(input("index for deleting??"))
            if delete >=1 and delete <= len(self.tasks):
                    self.tasks.pop(delete - 1) 
            else:
                print("invalid choice")


    def sortTask(self):
        self.tasks.sort(key=lambda task: datetime.strptime(task["due"],"%Y-%m-%d"))
    def viewTask(self):
        self.sortTask()
        today = date.today()
        for i, task in enumerate(self.tasks, start=1): #
            dueDate = datetime.strptime(task["due"], "%Y-%m-%d").date()
            overdue = " overdue !" if (dueDate < today and task["done"] == False) else ""
            countdown = dueDate - today
            print(f"{i}. {task["title"]}, Due: {task["due"]}, priority: {task["priority"]}, {overdue} {countdown.days} days remaining ")
        self.progress()
        self.showCompleted()
        self.showPending()


    def toggleTask(self):
        markComplete = int(input("number for task completion??"))  
        if markComplete >=1 and markComplete <= len(self.tasks):
            print(self.tasks[markComplete-1]["done"])
            self.tasks[markComplete-1]["done"] = not self.tasks[markComplete-1]["done"]
        else:
            print("invalid choice")

    def progress(self):
        progress = 0
        for task in self.tasks:
            if task["done"] == True:
                progress +=1
        print(f"{progress} /{len(self.tasks)} completed")

    def showCompleted(self):
        for task in self.tasks:
            if task["done"] == True:
                print(f"{task['title']} [✓]")

    def showPending(self):
        for task in self.tasks: 
            if task["done"] == False:
                print(f"{task['title']} []")

    def editTask(self):
        for i, task in enumerate(self.tasks, start=1):
            print(i,".", task["title"])
        taskToedit = int(input("Please enter which task do you want to edit "))
        if taskToedit >=1 and taskToedit <= len(self.tasks):
            taskToedit -= 1
            selectedTask = self.tasks[taskToedit]
            keys = list(selectedTask.keys())
            for i, key  in enumerate(keys, start=1):
                print(f"{i}. {key}")
            keyToedit = int(input("Please enter which value do you want to edit "))
            if keyToedit>=1 and keyToedit<= len(keys):
                keyToedit -=1
                actualKey = keys[keyToedit]
                print(f"Current Value :{selectedTask[actualKey]}")
                newValue = input("What do you want to replace with?")
                selectedTask[actualKey] = newValue

                print("task updated successfully")
            else:
                print("invalid field selection")
        else:
            print("invalid input")
    def searchTask(self):
        itemToSearch = input("Enter the task you want to search ")
        found = False
        for task in self.tasks:
            if itemToSearch.lower() in task["title"].lower():
                print(f"{task['title']} found")
                found = True
        if not found:
            print(f"{itemToSearch} not found")
    def saveTask(self):
        with open("tasks.json","w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent= 4)


#----------------ENDING FUNCTIONS

# MAIN--------------
tm = TASKMANAGER()
while True: 
    print("\n1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. toggle Task")
    print("5. edit Task")
    print("6. search Task")
    print("7. Exit")
        
    choice = int(input("Enter your choice "))

    if choice == 1:
        tm.addTask()
    elif choice == 2:
        tm.delTask()
    elif choice == 3:
        tm.viewTask()
    elif choice == 4:
        tm.toggleTask()
    elif choice == 5:
        tm.editTask()
    elif choice == 6:
        tm.earchTask()
    elif choice == 7:
        tm.saveTask()
        print("Exiting.....")
        break
    else:
        print("invalid input")
#---------------ENDING MAIN




# adding filter task feature