import os

def developSolutions(problem):
    print("------------------------------------------------------------------------")
    print("Now that we have gathered all the facts regarding the situations, it's time to come up with several solutions.\nIn this step, don't worry about the various impacts of solutions, just clearly outline all possible courses of actions. Remember, the more the better!")
    
    #restate problem
    print("To remind you, the problem that we're looking at is: %s" %problem)

    solFile = open("Potential_Solution", 'w')
    #print solutions to file
    solArray = getSolution(solFile)
    if(len(solArray) > 5): #TODO: compare length of array returned by getSolution
        solArray = analyseSolution(solFile, solArray)
    return solArray

def getSolution(solFile):
    solutionOpt = input("1 - add solution\n2 - next step\nEnter your input: ")
    solNum = 1
    solArray=[]
    while(solutionOpt != "2"):
        if(solutionOpt != "1"):
            print("Invalid input. You inputed '%s'" %solutionOpt)
            solutionOpt = input("1 - add solution\n2 - next step\nEnter your input: ")
        solution = input("Potential solution number %d: " %solNum)
        solFile.write("%d. %s\n" %(solNum, solution))
        solNum += 1
        solArray.append(solution)
        solutionOpt = input("1 - add solution\n2 - next step\nEnter your input: ")
    return solArray

def analyseSolution(solFile, solArray):
    solNum = len(solArray)
    print("\nYou have come up with %d potential solutions. Let's narrow it down to 5\n" %solNum)

    solFile.write("\nYou chose to eliminate these solutions:\n")
    while(len(solArray) > 5):
        print("Your potential solutions are:")
        for i in range(0,solNum):
            print("%d - %s" %(i+ 1, solArray[i]))
        eliminate = input("Enter the index of the potential solution that you want to elimniate: ")
        while(int(eliminate) < 1 or int(eliminate) > solNum):
            print("Invalid input. Your input must be between 1 and %d" %solNum)
            eliminate = input("Enter the index of the potential solution that you want to eliminate: ")
        
        deleted = solArray.pop(int(eliminate) - 1)
        solFile.write("%d. %s\n" %(int(eliminate), deleted))

        reason = input("Why do you choose to eliminate that potential solution?\nEnter your answer: ")
        solFile.write("Reason: %s\n"%reason)
    return solArray