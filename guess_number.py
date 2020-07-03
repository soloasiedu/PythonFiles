import random


print('Hello, What is your name')
name = input()
print('Well, '+name+' I am thinking of a number between 1 and 20')
print('Take a guess')
guessedNumber = input()
randomNumber = random.randint(1, 20)
guessAllowed = 6
guessesTaken = 1
while (int(guessedNumber) != randomNumber) and (guessesTaken < guessAllowed):
    if  int(guessedNumber) < randomNumber:
        print('Your guess is too low')
        guessesTaken = guessesTaken + 1
        print('Take a guess')
        guessedNumber = input()
    elif int(guessedNumber) > randomNumber:
        print('Your guess is too high')
        guessesTaken = guessesTaken + 1
        print('Take a guess')
        guessedNumber = input()
if guessesTaken < guessAllowed:
    print('Good job, '+ name+'! You guessed my number in '+str(guessesTaken)+ \
          ' attempt(s)') 
else:
    if int(guessedNumber) == randomNumber:
        print('Good job, '+ name+'! You guessed my number in '+str(guessesTaken)+ \
              ' attempt(s)') 
    else:
        print('Number of attempts exhausted!, The number I was guessing is '+ \
              str(randomNumber))
