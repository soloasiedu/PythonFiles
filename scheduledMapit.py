import time, datetime
import subprocess

timeToRunProgram = datetime.datetime(2020, 8, 13, 11, 1, 0)

while datetime.datetime.now() < timeToRunProgram:
    time.sleep(1)
subprocess.Popen([r'C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\python.exe', 'mapit.py', 'New York'])
