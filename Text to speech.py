import os
import speech_recognition as sr
from gtts import gTTS
import playsound
import pyaudio
import random
'''text to speech
Given input as text'''

def speak(bolo):
    x=str(random.randint(1,1100000))
    tts= gTTS(text= bolo , lang="en")     #convert the "text " file in to the audio file of language "en"(english).
    filename= "voice"+x+".mp3"                # Give a name to this file(audio file that is going to covert ).
    tts.save(filename)                   # Save this audiofile in your memory
    playsound.playsound(filename)         #play the coverted text
    
text=input("inser your text:")             #Take input   

speak(text)
