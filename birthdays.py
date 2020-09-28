


birthdays = {'Solomon': 'April 1', 'Beatrice': 'June 20', 'Laadi': 'April 18'}


while True:
    print('Enter name to get his/her birthday(blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for '+name)
        print('Enter the birthday of '+name)
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')



            
