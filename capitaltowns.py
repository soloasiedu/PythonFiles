import random


capitals = {'Western Region': 'Takoradi', 'Central Region': 'Cape Coast', \
        'Ashanti Region': 'Kumasi', 'Upper East Region': 'Bolgatanga', \
        'Upper West Region': 'Wa', 'Brong Ahafo Region': 'Sunyani', \
            'Eastern Region': 'Koforidua', 'Greater Accra Region': 'Accra', \
            'Volta Region': 'Ho', 'Northern Region': 'Tamale'}

regions = list(capitals.keys())
random.shuffle(regions)
for questNum in range(10):
    answer = capitals[regions[questNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(answer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [answer]
    random.shuffle(answerOptions)
    print(str(questNum + 1)+' What is capital of '+ regions[questNum]+'?')
    for i in range(4):
            print(f"{'ABCD'[i]}.{answerOptions[i]}")
    print('\n')
    print(f"{questNum + 1}.{'ABCD'[answerOptions.index(answer)]}")
    print('\n')


