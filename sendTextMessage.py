    


#messageBody = input('Enter the message you want to send: ')
#phoneNumberTo = input('Enter the phone number of the recipient eg. +233505883452: ')
accountSID = 'AC42cada35f6d8671e49f28bc512f57e00'
authToken = '5ad3626d8a958024f0abde3ac417ffa8'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+12513068264'
myCellPhone = '+233548660348'
message = twilioCli.messages.create(body= 'Hello Solomon, I am sending you this message from a python program I wrote', from_=myTwilioNumber, to=myCellPhone)
print('Message sent successfully')
