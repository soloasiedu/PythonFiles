def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number-sized
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me on 223-465-7890 landline or 355-567-5643 office number or 486-789-1111 \
home number'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: '+chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find phone number')



