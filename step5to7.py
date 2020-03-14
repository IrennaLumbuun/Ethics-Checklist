import os

def evalSolutions(solArr, shDict):
    print("------------------------------------------------------------------------")
    print("For each solution from the set of 5 solutions we have left, let's assign weights and benefits to the stakeholders.")
    print("- For the stakeholder weights, assign each stakeholder a weight from 1-9. Remember, these weights are relative to other stakeholders, so take the unbiased approach when assessing each stakeholder")
    print("- For the stakeholder benefits, assign each stakeholder a benefit from 1-9.")
    print("     - 9 means that the stakeholder associated has a MAJOR benefit from your solution, 5 is a NEUTRAL, 1 is a MAJOR Negative")
    print("     - A benefit could be monetary, moral (mental), physical (health), or any other factor that you deem worthy. This test does tend to take into account your biases if done incorrectly, so be wary of the biases found earlier")

    #open file to write evaluated solutions to
    evalFile = open("Evaluated_Solutions", 'w')
    evalFile.write("Evaluated solutions, stakeholder weights/benefits, and cumulative values\n")

    # create dictionary that will contain list of solutions and the weights,
    # benefits, and total values for each stakeholder
    evalSolutionsDict = {}

    # for each solution, assign weights and benefits to each stakeholder
    for solNum in range(len(solArr)):
        print("\nFor the solution \"%s\", assign weights and benefits to each stakeholder." %solArr[solNum])
        evalFile.write("Solution \"%s\":\n" %solArr[solNum])
        shWeightDict = {} # create dictionary of weights for the stakeholders
        shBeneDict = {} # create dictionary of benefits for the stakeholders
        shTotalDict = {} # create dictionary of total values for the stakeholders

        # assign weights and benefits to each stakeholder
        for name in shDict:
            #iterate through each stakeholder and assign weights/benefits to them
            evalFile.write("Stakeholder \"%s\": " %name)

            # get weight for current stakeholder
            print("\nAssign a weight (1-9) to stakeholder \"%s\"\n(motivation: %s)" %(name, shDict[name]))
            shWeight = int(input("Enter weight: "))
            while(shWeight > 9 or shWeight < 1):
                print("Invalid input. Your input: %d" %shWeight)
                shWeight = int(input("Enter weight: "))

            # add weight associated with name to dict
            shWeightDict[name] = shWeight

            # get benefit for current stakeholder
            print("Assign a benefit (1-9) to stakeholder \"%s\"" %name)
            shBenefit = int(input("Enter benefit: "))
            while(shBenefit > 9 or shBenefit < 1):
                print("Invalid input. Your input: %d" %shBenefit)
                shBenefit = int(input("Enter benefit: "))

            # add benefit associated with name to dict
            shBeneDict[name] = shBenefit

            # add total value associated with name to dict
            shTotalDict[name] = (shWeight*shBenefit)

            # write weight, benefit and total (weight*benefit) to file
            evalFile.write("weight - %d, benefit - %d, total - %d\n" %(shWeight, shBenefit, (shWeight*shBenefit)))

        # get cumulative total for the current solution
        solnCumulativeSum = 0
        for name in shTotalDict:
            solnCumulativeSum = solnCumulativeSum + shTotalDict[name]

        # write cumulative total for this solution to the file
        evalFile.write("Cumulative value for this solution: %d\n\n" %solnCumulativeSum)

        #add solution and stakeholders' weights and benefits to the solutions dict
        evalSolutionsDict[solArr[solNum]] = {'weights':shWeightDict, 'benefits':shBeneDict, 'totals':shTotalDict, 'sum': solnCumulativeSum}

    # pick optimal solution based on this initial evaluation
    solNum = 0
    maxSolutionSum = 0
    optimalSolution = "none"
    for soln in evalSolutionsDict:
        if(evalSolutionsDict[soln]['sum'] > maxSolutionSum):
            maxSolutionSum = evalSolutionsDict[soln]['sum']
            optimalSolution = soln

    print("According to this initial evaluation, the optimal solution is \"%s\"." %optimalSolution)
    print("""At this stage it is recommended to seek additional aid from peers and your respective disciplines ethics code.
    If applicable, it is also recommended to examine case studies similar to your situation.
    Lastly, if you believe that changes to this evaluation are in order after seeking assistance, you may repeat this step with modified weights and benefits if you wish.""")

    # close the file
    evalFile.close()
