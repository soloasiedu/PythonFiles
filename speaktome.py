import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander
import os

            
os.chdir(r'C:\Users\SOLO\Documents\PythonFiles')

running = True

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()



#play_audio('waterfall.wav')

r = sr.Recognizer()
cmd = Commander()
def initSpeech():
    print("Listening ...")
    play_audio("that-was-quick.wav")
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
    play_audio("clearly.wav")
    command = ""
    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you bro")
    print("Your command.")
    print(command)
    if command == "quit":
        running = False
    cmd.discover(command)
##    say('You said:' + command)

while running == True:
    initSpeech()

