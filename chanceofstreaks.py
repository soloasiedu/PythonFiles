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
                    break
      return isConsec



numberOfStreaks = 0
for i in range(10000):
    randomListHorT = getRandomListHorT()
    if containStreak(randomListHorT):
        numberOfStreaks += 1
    else:
        numberOfStreaks += 0

print('Chance of streak: %s' % (numberOfStreaks / 100))
