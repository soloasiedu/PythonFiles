
def findPairSum(list, sum):
    indexpairs = {}
    for i in range(len(list)-1):
        for j in range(1, len(list)):
            if (i < j) and list[i]+list[j] == sum:
                indexpairs[i] = j
                break
    return indexpairs

print(findPairSum([10,20,10,40,50,60,70], 60))
