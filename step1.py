import os 

#this method does part I of our checklist
def assembleFact():
    print("---------------------------------------------------------")
    #create a file consiting all the facts
    factFile = open("facts", 'w')

    #define the problem
    print("The first step of any investigation is to gather all facts in the situation. This is necessary to reveal previously unseen consequences or alternative interpretation")
    problem = input("In one brief sentence, state the problem: ")
    factFile.write("Problem:\n")
    factFile.write(problem +"\n")

    #add facts
    print("\nNow, can you think of some facts regarding this situation?")
    optFact = input("1 - add a fact\n2 - go to the next step\nEnter your input: ")
    factFile.write("\nFacts:\n")
    factNumber = 1
    while(optFact != "2"):
        if(optFact == "1"):
            addFact(factFile, factNumber)
            factNumber += 1
        else:
            print("Invalid input. You input: %s" %optFact)
        optFact = input("1 - add a fact\n2 - go to the next step\nEnter your input: ")
    if(factNumber == 1):
        factFile.write("No facts were gathered")

    #brainstorm problematic scenarios
    print("\nGreat! Let's think of some possible problematic scenarios if the problem remains unsolved")
    optScenario = input("1 - add a scenario\n2 - go to the next step\nEnter your input: ")
    factFile.write("\nProblematic Scenarios if problem is not solved:\n")
    scenNumber = 1
    while(optScenario != "2"):
        if(optScenario == "1"):
            addScenario(factFile, scenNumber)
            scenNumber += 1
        else:
            print("Invalid input. You input: %s" %optScenario)
        optScenario = input("1 - add a scenario\n2 - go to the next step\nEnter your input: ")
    if(scenNumber == 1):
        factFile.write("No scenarios were gathered")

    #anything else?
    print("\nYou're almost done with part I. Is there anything else you want to add regarding the situation?")
    misc = input("1 - Yes\n2 - No. Go to step 2\nEnter your input: ")
    if(misc == "1"):
        factFile.write("\nOther important stuff regarding the situation:\n")
        miscInput = input("Write it here: ")
        factFile.write(miscInput + "\n\n")
    
    print("\nWe're done with step 1. Continueing with step 2...")
    #close file
    factFile.close()
    return problem

#these function is called by assembleFact. It writes input to factFile
def addFact(factFile, factNumber):
    factFile.write(str(factNumber)+ ". ")
    fact = input("Fact number %d: " %factNumber)
    factFile.write(fact + "\n")

def addScenario(factFile, scenNumber):
    factFile.write("\n"+ str(scenNumber)+ ". ")
    scenario = input("Briefly describe the scenario: ")
    factFile.write(scenario + "\n")

    hasPerspective = 1
    print("\nLets take a look from other perspective to see how bias may emerge")
    hasPerspective = input("1 - add a perspective\n2 - Skip this step\nEnter your input: ")
    while (hasPerspective != "2"):
        if(hasPerspective != "1"):
            print("Invalid input. You input: %s" %hasPerspective)
            hasPerspective = input("1 - add more perspective\n2 - Next step\nEnter your input: ")

        povName = input("Whose perspective are you taking? ")
        factFile.write("Perspective of %s: " %povName)
        pov = input("Write down their perspective: ")
        factFile.write(pov +"\n")
        hasPerspective = input("1 - add more perspective\n2 - Next step\nEnter your input: ")
