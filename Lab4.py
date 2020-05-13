def minimumCheck(applyList):
    minWage = applyList[0][0]
    minPpl = 1
    jobPref = 1

    for i in range(len(applyList)):
        pplWage = applyList[i][0]
        pplJob = 1
        for j in range(len(applyList[i])):
            if applyList[i][j]<minWage:
                minWage = applyList[i][j]
                minPpl = i+1
                jobPref = j+1
            if applyList[i][j]<pplWage:
                pplWage = applyList[i][j]
                pplJob = j+1
        print("Minimum in People No.",i+1," is ",pplWage,"In job : ",pplJob)
                
    return print("Minimum in person No.",minPpl,"Minimum wage = ",minWage,"In job : " ,jobPref)
applyList = [[20,25,22,28],[15,18,23,17],[19,17,21,24],[58,23,24,24]]
print(minimumCheck(applyList))