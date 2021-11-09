import pyaudio
import pyttsx3
import  datetime
import speech_recognition as sr
import webbrowser as wb
import os
import pywhatkit
import pyjokes
import matplotlib.pyplot as plt
from tkinter import TclError
import struct
import numpy as np
import time

"""Speech Regconizer"""
friday=pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice',voice[0].id)

friday.save_to_file(text=str,filename='voicesaves.txt')
friday.runAndWait()

""" RATE"""
rate = friday.getProperty('rate')
friday.setProperty('rate',200)

def speak(audio):
    print('Assistant.: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def timenow():
    Time=datetime.datetime.now().strftime("%I: %M: %p")
    speak(Time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning")
    if hour >= 12 and hour < 18:
        speak("Good Afternoon")
    if hour >= 18 and hour < 24:
        speak("Good Evening ")
    speak('How can I help you?')
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 1
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("You: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command ")
        query = str(input('What you saying is:'))
    except sr.RequestError:
        speak("Sorry,my speech services is down")
    return query

if __name__ == "__main__":
    welcome()
    while True:
        query=command().lower()
        if"google" in query:
            speak("What should I search for you?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Google')
        if "youtube" in query:
            speak("What should I search for you?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Youtube')
        elif "play" in query:
            search = command().replace('play','')
            speak(f"playing {search}" )
            pywhatkit.playonyt(search)
        if "find location" in query:
            speak("What is the location?")
            search=command().lower()
            url = f"https://google.com/maps/search/{search}"
            wb.get().open(url)
            speak(f'Here is your location of {search}')
        if "time" in query:
            timenow()
        if "who are you" in query:
            speak("I am your voice Assistant")
        elif "joke" in query:
            speak(pyjokes.get_joke(category='all'))
        elif "reduce volume" in query:
            newVolume = 1
            while 1<= newVolume >=0:
                volume = friday.getProperty('volume')
                friday.setProperty('volume', newVolume)
                speak('Testing different voice volumes')
                friday.runAndWait()
                newVolume = newVolume - 0.2

        elif "increase volume" in query:
            newVolume = 1
            while newVolume >=0:
                volume = friday.getProperty('volume')
                friday.setProperty('volume', newVolume)
                speak('Testing different voice volumes')
                friday.runAndWait()
                newVolume = newVolume + 0.2
        if "quit" in query:
            speak("Exiting")
            exit()