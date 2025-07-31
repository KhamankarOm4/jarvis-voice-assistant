import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
import pygame
from gtts import gTTS
import os


# pip install SpeechRecognition
# pip install pyttsx3
# pip install pyaudio
# pip install pocketsphinx
# pip install requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "f645784f9bd7447aaff19f47b3d4aaba"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
   

def processCommand(c):
    if "open youtube" in c.lower():
        speak("Opening YouTube")
        time.sleep(1)
        webbrowser.open("https://www.youtube.com")

    elif "open google" in c.lower():
        speak("Opening Google")
        time.sleep(1)
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        time.sleep(1)
        webbrowser.open("https://www.facebook.com/")
    
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        time.sleep(1)
        webbrowser.open("https://instagram.com")

    elif "open twitter" in c.lower():
        speak("Opening Twitter")
        time.sleep(1)
        webbrowser.open("https://twitter.com")

    elif "open whatsapp" in c.lower():
        speak("Opening WhatsApp")
        time.sleep(1)
        webbrowser.open("https://web.whatsapp.com/")

    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        time.sleep(1)
        webbrowser.open("https://linkedin.com")
    
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        if link:
            speak(f"Playing {song}")
            time.sleep(1)
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song in the library.")
    elif "news" in c.lower():
        speak("Opening news")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            news_data = r.json()
            articles = news_data.get('articles', [])
            for article in articles:
                speak(article['title'])

    #else:
        
    

if __name__ == "__main__":
    speak("Initializing jarvis.......")
    
    while True:
        r= sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for command...")
                audio = r.listen(source,timeout=5, phrase_time_limit=4)
            word= r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes......")
                time.sleep(1)
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio2 = r.listen(source)
                    command = r.recognize_google(audio2)
                    processCommand(command)  
    
        except Exception as e:
            print(f"Error: {e}")
            speak("An error occurred. Please try again.")
            time.sleep(1)
     