import random


def getRandomListHorT():
    listOfHeadsOrTails = []
    for i in range(100):
      if random.randint(0,1) == 0:
            listOfHeadsOrTails.append('T')
      else:
            listOfHeadsOrTails.append('H')
    return listOfHeadsOrTails



def containStreak(list):
      isConsec = False
      for i in range(len(list)):
            if i == len(list)-6:
                  break
            else:
                firstItem = list[i]
                secondItem = list[i+1]
                thirdItem = list[i+2]
                fourthItem = list[i+3]
                fifthItem = list[i+4]
                sixthItem = list[i+5]
                if firstItem == secondItem and secondItem == thirdItem and \
                   thirdItem == fourthItem and fourthItem == fifthItem and \
                   fifthItem == sixthItem:
                    isConsec = True
                else:
                    isConsec = False
                if isConsec == True:
                    break
      return isConsec
                    

randomList = getRandomListHorT()
print(randomList)
if containStreak(randomList):
    print('This list contains six streaks of heads or tails')
else:
    print('This list has no six streaks of heads or tails')
