import os
import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("What would you like to do today")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening")
         r.pause_threshold=1
         audio=r.listen(source)
    try:
        print("recognizing")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query


if __name__ =="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open in' in query:
            webbrowser.open("linkedin.com")
        elif 'open hub' in query:
            webbrowser.open("github.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ,The time is {strTime}")
        elif 'open arduino' in query:
            codePath = "C:\\Users\\sansk\\OneDrive\\Desktop\\Arduino\\Arduino IDE.lnk"
            os.startfile(codePath)
        elif 'open code' in query:
            copath = "C:\\Users\\sansk\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(copath)