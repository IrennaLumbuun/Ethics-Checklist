#step 2 and 3 : Define stakeholders.
#stakeholders include anyone who might be affected by your action. It helps determine consequences of your decision
#-----------------------------------------------------------------------------------

import os

#this method guides user to figure out who are the stakeholders and call addSH
def stakeholders():
    print("-----------------------------------------------------------------")
    print("Let's define stakeholders; anyone who might be affected by your action.")
    print("This step is crucial to determine the short term and long term consequences of your decision")

    shFile = open("stakeholders", 'w')
    shFile.write("\nStakeholders:\n")
    shNumber = 1
    shDict = {}

    #customers
    print("Does the problem have the possibility to affect customers?")
    customer = input("1 - yes\n2 - no\nEnter your input: ")
    while(customer != "1" and customer != "2"):
        customer = input("1 - yes\n2 - no\nEnter your input: ")

    if(customer == "1"):
        print("Any particular groups of customers over others?")
        customer = input("1 - yes\n2 - no\nEnter your input: ")
        while(customer != "1" and customer != "2"):
            customer = input("1 - yes\n2 - no\nEnter your input: ")
        if(customer == "1"):
            name =  input("Name of the group: ")
            addSH(shFile, shNumber, name, shDict)
            shNumber += 1
        else:
            addSH(shFile, shNumber, "customer", shDict)
            shNumber += 1
    
    #people at the company
    print("\nDoes the problem affect people at your company? (Think of your collegues, people above you, and people below you)")
    stakeholder = input("1 - add a person\n2 - go to the next step\nEnter your input: ")
    while(stakeholder != "2"):
        if(stakeholder == "1"):
            name = input("Name of stakeholder: ")
            addSH(shFile, shNumber, name, shDict)
            shNumber += 1
        else:
            print("Invalid input. You input: %s" %stakeholder)
        stakeholder = input("1 - add another person\n2 - go to the next step\nEnter your input: ")
    
    #society
    print("\nDoes the problem have the possibility to affect society? (Particular group, particular country, everyone?)")
    stakeholder = input("1 - add a stakeholder\n2 - go to the next step\nEnter your input: ")
    while(stakeholder != "2"):
        if(stakeholder == "1"):
            name = input("Name: ")
            addSH(shFile, shNumber, name, shDict)
            shNumber += 1
        else:
            print("Invalid input. You input: %s" %stakeholder)
        stakeholder = input("1 - add a stakeholder\n2 - go to the next step\nEnter your input: ")
    
    #people close to you
    print("\nDoes the problem have the possibility to affect people close to you?")
    stakeholder = input("1 - add a person\n2 - go to the next step\nEnter your input: ")
    while(stakeholder != "2"):
        if(stakeholder == "1"):
            name = input("Name of the person: ")
            addSH(shFile, shNumber, name, shDict)
            shNumber += 1
        else:
            print("Invalid input. You input: %s" %stakeholder)
        stakeholder = input("1 - add a person\n2 - go to the next step\nEnter your input: ")
    
    #other entities
    print("\nDoes the problem have the possibility to affect other entities?")
    stakeholder = input("1 - add a stakeholder\n2 - go to the next step\nEnter your input: ")
    while(stakeholder != "2"):
        if(stakeholder == "1"):
            name = input("Name of the entity: ")
            addSH(shFile, shNumber, name, shDict)
            shNumber += 1
        else:
            print("Invalid input. You input: %s" %stakeholder)
        stakeholder = input("1 - add a stakeholder\n2 - go to the next step\nEnter your input: ")
    
    #other groups not covered previously
    print("\nAnyone else?")
    stakeholder = input("1 - add a stakeholder\n2 - go to the next step\nEnter your input: ")
    while(stakeholder != "2"):
        if(stakeholder == "1"):
            name = input("Name of stakeholder: ")
            addSH(shFile, shNumber, name, shDict)
            shNumber += 1
        else:
            print("Invalid input. You input: %s" %stakeholder)
        stakeholder = input("1 - add a stakeholder\n2 - go to the next step\nEnter your input: ")
    
    #yourself
    print("\nLastly, let's put you on the list because you are involved. You are also a stakeholder")
    addSH(shFile, shNumber, "You", shDict)

    #done
    print("\nWe are done with step 2 and step 3!")
    shFile.close()
    return shDict

#this method guides users to figure out stakeholder's motivation and then write them down to the file
def addSH(shFile, shNumber, name, shDict):
    shFile.write("%d. %s\n" %(shNumber, name))
    print("Everyone has personal, position-related, financial, or political motivations. Think of the motivation of %s. You can put N/A if it's irrelevant or if you can't think of any" %name)
    pMotiv = input("\nWhat is this stakeholder's personal motivation?\n")
    posMotiv = input("\nGreat. \nWhat is this stakeholder's position related motivations?\n")
    finMotiv = input("\nWhat is this stakeholder's financial motivations?\n")
    polMotiv = input("\nWhat is this stakeholder's political motivations?\n")

    motivArr = [pMotiv, posMotiv, finMotiv, polMotiv]

    print("\nGood job! You have identified %s's motivations.")
    print("Their personal motivation is %s, position related motivation is %s, financial motivation is %s, and political motivation is %s" %(pMotiv, posMotiv, finMotiv, polMotiv))
    mostReasonable = input("""\nOut of these four motivations, pick one that you think is the most reasonable potential motvations?
    1 - personal motivation
    2 - position related motivation
    3 - financial motivation
    4 - political motivation
    Enter your input: """)
    try:
        while(int(mostReasonable)< 1 or int(mostReasonable) > 4):
            print("Invalid input. You inputed '%s'" %(mostReasonable))
            mostReasonable = input("""Out of the four motivations, pick one that you think is the most reasonable potential motvations?
            1 - personal motivation
            2 - position related motivation
            3 - financial motivation
            4 - political motivation
            Enter your input: """)
    except ValueError:
        print("Invalid input. You inputed '%s'" %(mostReasonable))
        mostReasonable = input("""Out of the four motivations, pick one that you think is the most reasonable potential motvations?
        1 - personal motivation
        2 - position related motivation
        3 - financial motivation
        4 - political motivation
        Enter your input: """)

    
    shFile.write("personal motivation: %s\nPosition related motivation: %s\nFinancial motivation: %s\nPolitical motivation: %s" %(pMotiv, posMotiv, finMotiv, polMotiv))
    shFile.write("\nMost Reasonable: %s\n" %motivArr[int(mostReasonable) - 1])
    shDict[name] =  motivArr[int(mostReasonable) - 1]
    return shDict
