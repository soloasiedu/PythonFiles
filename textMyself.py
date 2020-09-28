accountSID = 'AC42cada35f6d8671e49f28bc512f57e00'
authToken = '5ad3626d8a958024f0abde3ac417ffa8'
myTwilioNumber = '+12513068264'
myCellPhone = '+233548660348'
from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    message = twilioCli.messages.create(body= message,from_=myTwilioNumber, to=myCellPhone)
