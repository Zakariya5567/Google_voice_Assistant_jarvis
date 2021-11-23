from math import e
from sys import path
import pyttsx3
# text to speech conversation library

import speech_recognition as sr
# speach recognition library is use to take microphone input from the user
#  and return string output
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
# sapi5 is a speech application programming interface (Api) to allow the use of speach recognition and speach synthesis
#pyttsx3.init function to load cinversation

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
# speak function use to speak the given input
#runAndWait(): This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you
    engine.say(audio)
    engine.runAndWait()


def wishMe():
# wishme function is use to wish a user according to time

    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis. please tell me how may i help you")

def sendEmail(to, content):
    
    server=smtplib.SMTP('smtp.gmail.com',587)   
    server.ehlo()
    #Use the EHLO command to identify the domain name of the sending host to SMTP before you issue a MAIL FROM command.
    server.starttls()
    #The StartTLS command can be used to initiate encrypted e-mail communication based on the TLS protocol
    server.login('mdzakariya333@gmail.com',"zakariya5567")
    #sender email and password
    server.sendmail('mdzakariya333@gmail.com',to,content)
    #sender email, reciever email, and content(message)
    server.close()

def takeCommand():
# take commnad fuction use for to take input from the user and convert it
# to text

    r = sr.Recognizer()
# r is a instance variable of speech recognizer class

    with sr.Microphone() as source:
    # use microphone is a source

        print("Listning.......")
        r.pause_threshold = 1
        #Using this method you can adjust the energy threshold dynamically using audio from the source to get an ambient noise.
        audio=r.listen(source)
        #listen() method which puts the server into listen mode. This allows the server to listen to incoming connections
    try:
        print("Recognizing.......")
        query=r.recognize_google(audio,language="en-in")
        #using the Google Speech Recognition API and Performs speech recognition on audio_data
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please")
        return "None"
    return query

    
    
if __name__=="__main__":
    wishMe() 
    while True:
        query = takeCommand().lower()
        #lower() is a built-in method used for string handling. it returns the lowercased string from the given string.
        #It converts all uppercase characters to lowercase
        if 'wikipedia' in query:
             print("searching wikipedia")
             query=query.replace("wikipedia","")
             results=wikipedia.summary(query,sentences=2)
             speak("according to wikipedia")
             print(results)
             speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'play music' in query:
            music_dir='E:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is  {strTime}")
        
        elif 'open code' in query:
            codePath='C:\\Users\\Md zakariya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = 'zakariya5567@gmail.com'
                sendEmail(to , content)
                speak("your email has been sent")
            except Exception as e:
                print(e)
                speak("sorry unable to sent email")

