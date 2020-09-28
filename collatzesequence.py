

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1


try:
    userNumber = int(input('Enter a number: '))
    while userNumber != 1:
        userNumber = collatz(userNumber)
        collatz(userNumber)
except ValueError:
    print('You must enter an integer')

    
    
    

