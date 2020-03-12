#this program creates a directory containing user's ethics checklist
#when the program is run, users can opt to review their existing checklist
#or create a new ethics checklist

#-------------------------------------------------------------------------
import os

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
            
            #part 1: Fact Assembly
            assembleFact()

        #user chooses to update their preexisting checklist. Do part 5 - 10
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

#this method does part I of our checklist
def assembleFact():
    print("---------------------------------------------------------")
    #create a file consiting all the facts
    factFile = open("step1_assembleFacts", 'w')

    #define the problem
    print("The first step of any investigation is to gather all facts in the situation. This is necessary to reveal previously unseen consequences or alternative interpretation")
    problem = input("In one brief sentence, state the problem: ")
    factFile.write("Problem:\n")
    factFile.write(problem +"\n")

    #add facts
    print("Now, can you think of some facts regarding this situation?\n")
    optFact = input("1 - add a fact\n2 - go to the next step\n")
    factFile.write("\nFacts:\n")
    factNumber = 1
    while(optFact != "2"):
        if(optFact == "1"):
            addFact(factFile, factNumber)
            factNumber += 1
        else:
            print("Invalid input. You input: %s" %optFact)
        optFact = input("1 - add a fact\n2 - go to the next step\n")
    if(factNumber == 1):
        factFile.write("No facts were gathered")

    #brainstorm problematic scenarios
    print("Great! Let's think of some possible problematic scenarios if the problem remains unsolved")
    optScenario = input("1 - add a scenario\n2 - go to the next step\n")
    factFile.write("\nProblematic Scenatios if problem is not solved:\n")
    scenNumber = 1
    while(optScenario != "2"):
        if(optScenario == "1"):
            addScenario(factFile, scenNumber)
            scenNumber += 1
        else:
            print("Invalid input. You input: %s" %optScenario)
        optScenario = input("1 - add a fact\n2 - go to the next step\n")
    if(scenNumber == 1):
        factFile.write("No facts were gathered")

    #anything else?
    print("You're almost done with part I. Is there anything else you want to add regarding the situation?")
    misc = input("1 - Yes\n2 - No. Go to step 2")
    if(misc == "1"):
        factFile.write("\Other important stuff regarding the situation:\n")
        miscInput = input("Write it here: ")
        factFile.write(miscInput + "\n\n")
    #close file
    factFile.close()

#these function is called by assembleFact. It writes input to factFile
def addFact(factFile, factNumber):
    factFile.write(str(factNumber)+ ". ")
    fact = input("Fact number %d: " %factNumber)
    factFile.write(fact + "\n")

def addScenario(factFile, scenNumber):
    factFile.write(str(scenNumber)+ ". ")
    scenario = input("Briefly describe the scenario: ")
    factFile.write(scenario + "\n")

    hasPerspective = 1
    print("Lets take a look from other perspective to see how bias may emerge")
    hasPerspective = input("1 - add a perspective\n2 - Skip this step\n")
    while (hasPerspective != "2"):
        if(hasPerspective != "1"):
            print("Invalid input. You input: %s" %hasPerspective)
            hasPerspective = input("1 - add more perspective\n2 - Next step\n")

        povName = input("Whose perspective are you taking? ")
        factFile.write("Perspective of %s: " %povName)
        pov = input("Write down their perspective: ")
        factFile.write(pov +"\n")
        hasPerspective = input("1 - add more perspective\n2 - Next step\n")

greeting()