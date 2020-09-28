

print('Enter a list of integers!')
print('Enter stop to stop listing numbers!')


listofNumbers = []

userInput = input()
while userInput != 'stop':
    listofNumbers.append(int(userInput))
    userInput = input()

for i in range(len(listofNumbers)):
    print(listofNumbers[i])

print('\n')
print(listofNumbers[-1])
print('\n')
listofNumbers.reverse()
for i in range(len(listofNumbers)):
    print(listofNumbers[i])
print('\n')
listofNumbers.sort()
for i in range(len(listofNumbers)):
    print(listofNumbers[i])


def contains5(list):
    for i in range(len(list)):
        if list[i] == 5:
            return True
    return False


def numberof5s(list):
    count = 0
    for i in range(len(list)):
        if list[i] == 5:
            count = count + 1
    return count

print(numberof5s(listofNumbers))
print(contains5(listofNumbers))
