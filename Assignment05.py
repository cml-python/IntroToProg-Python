# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# cleung,17May2020,Added code to complete Assignment05
# ------------------------------------------------------------------------ #
# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}# A row of data separated into elements of a dictionary {Task,Priority}
firstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
#loadFile= open(objFile,"r")
#for row in loadFile:
 #   firstrow = row.split(",")
  #  dicRow= {'Task':firstrow[0], 'Priority':firstrow[1].strip()}
   # firstTable.append(dicRow)
#loadFile.close()
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
        for dicRow in firstTable:
            print("Task: "+dicRow["Task"]+"\t"+"Priority: "+dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task= input("Task: ")
        priority= input("Priority: ")
        dicRow= {"Task": task, "Priority": priority}
        firstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("Current Tasks: ")
        for row in firstTable:
            print('\t'+row["Task"])
        removeTask= input("Task to Remove: ").lower()
        for dicRow in firstTable:
            if dicRow["Task"].lower() == removeTask:
                firstTable.remove(dicRow)
                print("Task Removed.")
        if removeTask is None:
            print("Task Doesn't Exist")
        else:
            continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        loadFile= open("ToDoList.txt","w")
        for dicRow in firstTable:
            loadFile.write("Task: "+dicRow["Task"]+"\t"+"Priority: "+dicRow["Priority"]+'\n')
        loadFile.close()
        print("Data Saved")
        continue
# Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Press Enter to Exit")
        break  # and Exit the program