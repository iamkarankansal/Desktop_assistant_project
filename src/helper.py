# import pyttsx3 #for text to speech conversion
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os

# # #to upload code on github:
# #git add .
# #git commit -m "msg"
# #git push origin main

# # Take voice from system
# engine=pyttsx3.init('sapi5') #engine is object, and this line is for initialize pyttsx3
# voices=engine.getProperty('voices') #take speech form system and create a list voices, link contain voice object , use by voice[].id
# # print(voices)
# # print(voices[0].id) #male voice DAVID
# # print(voices[1].id) #female voice ZIRA

# #to set male voice:
# engine.setProperty('voice',voices[0].id)
# engine.setProperty('rate', 170) #to change speed of speaking
# #speak function:
# def speak(text):
#     engine.say(text)
#     engine.runAndWait() #to stop speech function

# #speech recognition function
# def takeCommand():
#     """this function will recognize voice & return text
#     """
#     r=sr.Recognizer()
#     with  sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold=1    #stops hearing after 1 sec of stop speaking
#         audio=r.listen(source) #this uses google free api default: speech to text

#         try:
#             print("Recognize...")
#             query=r.recognize_google(audio,language='en-in')
#             print(f"User said: {query}\n")

#         except Exception as e:
#             print("Say again...")
#             return "None"
#         return query
# # text=takeCommand()
# # speak(text)

# #The function for wish me by using time
# def wish_me():
#     hour = (datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good morning sir. How are you doing.")
    
#     elif hour>=12 and hour<18:
#         speak("Good afternoon sir. How are you doing.")

#     else:
#         speak("Good evening sir. How are you doing.")
    
#     speak("Tell me sir how can i help you")











# ____________________________________________________BY GOOGLE API: GEMINI_____________________________________________________________






import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS


GOOGLE_API_KEY = "AIzaSyCqwpcMsImZqWgYqlx5QOueECh1wysYS3I"
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY


def voice_input():
    # Create a recognizer instance
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)  # Using Google Speech Recognition
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    

def text_to_speech(text):
    # Create a gTTS object
    tts = gTTS(text=text, lang='en')  # Language can be changed

    # Save the audio as an MP3 file
    tts.save("speech.mp3")



def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')
    
    response=model.generate_content(user_text)
    
    result=response.text
    
    return result
    