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
            elif list[i] != list[i+5] or list[i+1] != list[i+4] or list[i+2] != list[i+3]:
                continue
            else:
                if list[i] == list[i+1] and list[i+1] == list[i+2]and \
                   list[i+2] == list[i+3]and list[i+3] == list[i+4] and \
                   list[i+4] == list[i+5]:
                    isConsec = True
                    break
      return isConsec



numberOfStreaks = 0
for i in range(1000000):
    randomListHorT = getRandomListHorT()
    if containStreak(randomListHorT):
        numberOfStreaks += 1
    else:
        numberOfStreaks += 0

print('Chance of streak: %s' % (numberOfStreaks / 10000))
