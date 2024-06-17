import pyttsx3 #for text to speech conversion
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Take voice from system
engine=pyttsx3.init('sapi5') #engine is object, and this line is for initialize pyttsx3
voices=engine.getProperty('voices') #take speech form system and create a list voices, link contain voice object , use by voice[].id
# print(voices)
# print(voices[0].id) #male voice DAVID
# print(voices[1].id) #female voice ZIRA

#to set male voice:
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 150) #to change speed of speaking
#speak function:
def speak(text):
    engine.say(text)
    engine.runAndWait() #to stop speech function

#speech recognition function
def takeCommand():
    """this function will recognize voice & return text
    """
    r=sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1    #stops hearing after 1 sec of stop speaking
        audio=r.listen(source) #this uses google free api default: speech to text

        try:
            print("Recognize...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say again...")
            return "None"
        return query
text=takeCommand()
speak(text)