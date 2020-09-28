import time, datetime

timeToRunProgram = datetime.datetime(2020, 8, 12, 23, 28, 0)

while datetime.datetime.now() < timeToRunProgram:
    time.sleep(1)
print('Programming now starting at 11:28')
