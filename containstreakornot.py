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
      isConsec = True
      for i in range(len(list)):
            if i == len(list)-6:
                  break
            else:
                  for y in range(5):
                        currentItem = list[i+y]
                        currentItemPlusOne = list[i+(y+1)]
                        if currentItem != currentItemPlusOne:
                              isConsec = False
                        else:
                            isConsec = True
                  if isConsec == True:
                      break
      return isConsec

randomList = getRandomListHorT()
print(randomList)
if containStreak(randomList):
    print('This list contains six streaks of heads or tails')
else:
    print('This list has no six streaks of heads or tails')


