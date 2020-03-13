#this program creates a directory containing user's ethics checklist
#when the program is run, users can opt to review their existing checklist
#or create a new ethics checklist

#-------------------------------------------------------------------------

import os
from step1 import assembleFact
from step2and3 import stakeholders
from step4 import developSolutions

#this method greets user and and ask if they want to create a new checklist orupdate pre-existing one
#it verifies that users input the right value, and then return the input
def greeting():
    validInput = False
    print("Welcome to the program!\n1 - Create a new Ethics Checklist\n2 - Update pre-existing checkllist\n3 - quit")
    userInput = input("Enter your input: ")

    while(validInput == False):
        #user chooses to create a new ethics checklist. Do part 1 - 4
        if(userInput == "1"):
            validInput = True
            #part 0: create the folder
            print("---------------------------------------------------------")
            print("You chose to create a new ethics checklist. Generating...")
            path = createFolder()
            os.chdir(path)
            print("success creating folder")

            #step 1: Fact Assembly
            problem = assembleFact()

            #step 2 and 3: Define Stakeholders
            stakeholders()

            #step 4: develop Solutions
            solArray = developSolutions(problem)
            print("remaining solutions: ")
            print(solArray)

        #user chooses to update their preexisting checklist. Do part 6 - 8
        elif(userInput == "2"):
            validInput = True
            print("input is 2")

        #user chooses to exit
        elif(userInput == "3"):
            exit()

        #invalid input
        else:
            print("Invalid input: you inputed '%s'" %userInput)
            print("1 - Create a new Ethics Checklist\n2 - Update pre-existing checkllist\n3 - quit")
            userInput = input("Enter your input: ")

#this function is called when users opt to create a new ethics checklist
#it creates a new folder in current directory, and return its path
def createFolder():
    folderName = input("Enter the name of this ethics checklist: ")
    path = os.path.join(os.getcwd(), folderName)
    try:
        os.mkdir(path)
    except OSError as error:
        print("Error creating a folder -- %s" %error)
        createFolder()
    return path

greeting()