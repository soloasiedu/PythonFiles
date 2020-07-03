print('How many dogs do you have?')
number = input()
while number != '':
    try:
        if int(number) > 5:
            print('You have many dogs')
        elif int(number) >= 0 and int(number) <= 5:
            print('You dont have many dogs')
        else:
            print('You cant have negative number of dogs')
    except ValueError:
        print('You did not enter a number')
    print('How many dogs do you have?')
    number = input()
