while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Enter a number for your age')

while True:
    print('Enter a password')
    password = input()
    if password.isalnum():
        break
    print('Enter a password containing letters or numbers only')
