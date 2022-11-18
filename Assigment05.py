# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.20xx,Created started script
# AYi, 11.16.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""   # A row of text data from the file
Data = ""      # A temporary variable to save key
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
TempRow = ""   # A temporary variable to save a row in lstTable
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
prvData = ""   # A Capture of task to be removed


'''
#This is the Code to create the initial text file

intFile = open(objFile, "w")
dicRow = {"Task": "Dishes", "Priority": "3"}
intFile.write(dicRow["Task"] + '-' + dicRow["Priority"] + '\n')
dicRow = {"Task": "Laundry", "Priority": "4"}
intFile.write(dicRow["Task"] + '-' + dicRow["Priority"] + '\n')
intFile.close()
'''

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# TODO: Add Code Here
intFile = open(objFile, "r")
for strData in intFile:
    Data = strData.split("-")
    dicRow = {"Task": Data[0].strip(), "Priority": Data[1].strip()}
    lstTable.append(dicRow)
intFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save data to file
    5) Exit program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):

        # TODO: Add Code Here
        print("Current To Do List:")
        print("-------------------")
        i = 0
        while(i < len(lstTable)):
            TempRow = lstTable[i]
            print(TempRow["Task"] + " - " + TempRow["Priority"])
            i += 1
        print()
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):

        # TODO: Add Code Here
        while(True):
            Task = input("Add a task: ")
            Priority = input("""
            Select priority level for this task: 
            1-Urgent | 2-High | 3-Medium | 4-Low
            """)
            if(Priority.lower() == '1' or Priority.lower() == '2' or Priority.lower() == '3' or Priority.lower() == '4'):
                dicRow = {"Task": Task, "Priority": Priority}
                lstTable.append(dicRow)
                break
            else:
                print("Please select 1, 2, 3, or 4 for task prioritization!")
                print()
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):

        # TODO: Add Code Here
        print("This is the current to-do list:")
        print("-------------------------------")
        i = 0
        while (i < len(lstTable)):
            TempRow = lstTable[i]
            print(TempRow["Task"] + " - " + TempRow["Priority"])
            i += 1
        print()
        PrvData = input("What task would you like to remove?: ")
        j = 0
        while (j < len(lstTable)):
            TempDicRow = lstTable[j]
            if(TempDicRow["Task"].lower() == PrvData.lower()):
                lstTable.remove(TempDicRow)
                print("Successfully deleted!")
            else:
                if (j == len(lstTable)-1):
                    print()
                    print("'" + PrvData + "'" + " not found!")
            j += 1
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):

        # TODO: Add Code Here
        intFile = open(objFile, "w")
        i = 0
        while (i < len(lstTable)):
            TempRow = lstTable[i]
            intFile.write(TempRow["Task"] + " - " + TempRow["Priority"] + "\n")
            i += 1
        intFile.close()
        print()
        print("The changes you made were saved!")
        print()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):

        # TODO: Add Code Here
        strMenu = input("Are you sure you want to exit?[y/n]: ")
        if(strMenu.lower() == "yes" or strMenu.lower() == "y"):
            break
        else:
            continue

    else:
        print()
        print("Error! " + strChoice + " is not an option.")
        continue