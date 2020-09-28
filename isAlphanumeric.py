#! python3
import re

stringToSearch = input('Enter a string to check if it is alphanumeric: ')
alphanumericRegex = re.compile(r'(^[a-zA-Z0-9]$)+')
mo = alphanumericRegex.search(stringToSearch)

if mo == None:
    print(stringToSearch + ' is not alphanumeric')
else:
    print(stringToSearch + ' is alphanumeric')
