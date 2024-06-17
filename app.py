# from src.helper import speak, takeCommand, wish_me

# import pyttsx3 #for text to speech conversion
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os
# import streamlit as st



# #industry level code
# if __name__=="__main__":
#     wish_me()
#     # while "end" or "and" not in query: #it is always true since, "end" is non-empty string
#     # while "end" not in query and "and" not in query: #use this
#     while True:

#         st.title("Desktop Assistent System")

#         query=takeCommand().lower()
#         if "wikipedia" in query:
#             speak("Searching wikipedia")
#             query=query.replace('wikipedia',"")
#             results=wikipedia.summary(query,sentences=2)
#             speak("According to wikipedia")
#             print(results)
#             speak(results)
#         elif "youtube" in query:
#             speak("Opening youtube")
#             webbrowser.open("youtube.com")
#         elif "google" in query:
#             speak("Opening google")
#             webbrowser.open("google.com")
#         elif "github" in query:
#             speak("Opening github")
#             webbrowser.open("github.com")
#         elif 'time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"Sir the time is {strTime}")
#         elif "goodbye" in query:
#             speak("Bye Bye")
#             exit()

#-----------------------------------------------------------------------BY API------------------------------------------------------------------


import streamlit as st 
from src.helper import voice_input, text_to_speech, llm_model_object


def main():
    st.title("Multilingual AI Assistant")

    if st.button("Ask me anything!"):
        with st.spinner("Listening..."):
            text = voice_input()
            response = llm_model_object(text)
            text_to_speech(response)


            # Display audio player and download link
            audio_file = open("speech.mp3", 'rb')
            audio_bytes = audio_file.read()
            
            st.text_area(label="Response:", value=response, height=350)
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button(label="Download Speech",
                                data=audio_bytes,
                                file_name="speech.mp3",
                                mime="audio/mp3")









if __name__ == "__main__":
    main()