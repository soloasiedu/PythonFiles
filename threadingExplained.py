import threading, time

print('Start of program')
def takeANap():
    time.sleep(10)
    print('Wake up')
threadObj = threading.Thread(target = takeANap)
threadObj.start()
print('End of program')
