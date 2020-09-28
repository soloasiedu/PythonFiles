import random, time
import pyinputplus as pyip


numberOfQuestions = 10
correctAnswers = 0


for questionNumber in range(numberOfQuestions):
    firstNumber = random.randint(0,9)
    secondNumber = random.randint(0,9)
    answer = firstNumber * secondNumber
    print('What is '+ str(firstNumber) + ' * ' + str(secondNumber) + '?')
    response = int(input())
    if response == answer:
        correctAnswers += 1
        print('Yes!!, The correct answer is '+ str(answer))
    else:
        correctAnswers += 0
        print('Sorry, The correct answer is '+ str(answer))

print('You scored ' + str(correctAnswers) + 'correct answers out of ' + \
      str(numberOfQuestions) + ' questions')

