import time
import os
pw1=90588
pw2=56346
pw3=32322
print("\u001b[33;1m**************************************************************************************\n\n")
print("\u001b[33;1m _____     ______     _______    _______                 ________     ______     _____")
print("\u001b[33;1m|     |   |      |    |         |         |         |   |        |   |      |   |     \ ")
print("\u001b[33;1m|_____|   |      |    |         |         |         |   |        |   |______|   |      \ ")
print("\u001b[33;1m|         |------|    |-----|   |-----|   |         |   |        |   |   \      |       |")
print("\u001b[33;1m|         |      |          |         |   |    |    |   |        |   |    \     |      / ")
print("\u001b[33;1m|         |      |   _______|  _______|   |____|____|   |________|   |     \    |_____/ \n\n")
print("Enter the password to proceed")
pw=int(input())
if pw == pw1 or pw == pw2 or pw == pw3:
    os.system("cls")
else:
    os.system("cls")
    print("\u001b[31;1m \t\t\t\t             ___ ")
    print("\u001b[31;1m \t\t\t\t            |   |")
    print("\u001b[31;1m \t\t\t\t            |   |")
    print("\u001b[31;1m \t\t\t\t            |   |")
    print("\u001b[31;1m \t\t\t\t ___   ___  |   |  ___")
    print("\u001b[31;1m \t\t\t\t|   | |   | |   | |   |")
    print("\u001b[31;1m \t\t\t\t|   | |   | |   | |   |")
    print("\u001b[31;1m \t\t\t\t|   | |   | |   | |   | ___")
    print("\u001b[31;1m \t\t\t\t|   | |   | |   | |   ||   |")
    print("\u001b[31;1m \t\t\t\t|   | |   | |   | |   ||   |")
    print("\u001b[31;1m \t\t\t\t|   | |   | |   | |   ||   |")
    print("\u001b[31;1m \t\t\t\t\                         /")
    print("\u001b[31;1m \t\t\t\t \                       /")
    print("\u001b[31;1m \t\t\t\t  \                     /")
    print("\u001b[31;1m \t\t\t\t   \                   /")
    print("\u001b[31;1m \t\t\t\t    \                 /")
    print("\u001b[31;1m \t\t\t\t     \               /")
    print("\u001b[31;1m \t\t\t\t      \             /")
    print("\u001b[31;1m \t\t\t\t       \___________/")

    time.sleep(5)
    exit()



import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

print("\u001b[34;1m\t\t\t _______     ________     _            _______      ______     ")
print("\u001b[34;1m\t\t\t|       |    |      |    | \     |    |       |    |      \    ")
print("\u001b[34;1m\t\t\t|       |    |______|    |  \    |    |       |    |       \   ")
print("\u001b[34;1m\t\t\t|-------|    |   \       |   \   |    |-------|    |-------|   ")
print("\u001b[34;1m\t\t\t|       |    |    \      |    \  |    |       |    |       /   ")
print("\u001b[34;1m\t\t\t|       |    |     \     |     \_|    |       |    |______/\n\n")
print("\u001b[32;1m\t\t\t\t\tCreated by-Arnab")
print("\u001b[32;1m\t\t\t\t\t-I am not responsible for and damage\n\n\n")


def speak(text):
    tts=gTTS(text=text,lang='en')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

speak("Hello I am a Desktop Assistant")
speak("I can help you manage your desktop\n\n")
