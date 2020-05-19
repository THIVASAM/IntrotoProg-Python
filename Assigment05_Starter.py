# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Thivanka Samaranayake, 05/16/2020, Completed Step1
# Thivanka Samaranayake, 05/17/2020, Completed Step2-5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
print("Loading Data into a Dictionary Object")
objNewFile = open("ToDoList.txt", "r")
for row in objNewFile:
    task,priority = row.split(",")
    dicRow = {"Task": task, "Priority": priority.strip()}
    lstTable.append(dicRow)
    #print(lstTable) To test code print out the list
objNewFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow ["Task"] + "," + dicRow["Priority"])
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while strChoice == '2':
            strNewTask = input("Enter a new task: ")
            strNewPriority = input("Enter the priority level for task: ")
            lstTable.append({"Task": strNewTask, "Priority": strNewPriority})
            strNewChoice = input("Would you like to add any more tasks? ("'Y/N'")")
            if strNewChoice.lower() == 'n':
                break
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        while strChoice == '3':
            strTask = input("Task to Remove: ")
            for dicRow in lstTable:
                if dicRow ["Task"].lower() == strTask.lower():
                    break #This break stops the for loop

            lstTable.remove(dicRow)
            print("The task is removed")
            strNewChoice = input("Would you like to exit this choice ('Y/N')")
            if strNewChoice.lower() == 'y':
                break
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"] + '\n'))
        objFile.close()
        #continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("The Program Has Ended")
        input("\nPress Enter to exit")
        break  # and Exit the program
