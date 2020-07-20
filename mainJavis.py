import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


print("Initializing Javis")

MASTER = "Potter"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good morning" + MASTER)
    elif hour>=12 and hour<18:
         speak("Good afternoon" + MASTER)
    else:
         speak("Good evening" + MASTER)
    # speak("I am Jarvis. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en')
        print(f"user said: {query}\n")


    except Exception as e:
        print("say that again please")
        query = None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ndpnguyen.17ce@sict.udn.vn','sict123456')
    server.sendmail('dpbao.17it3@sict.udn.vn', to, content)
    server.close()



speak("initalizing Jarvis.....")
wishMe()
query = takeCommand()


if 'wikipedia' in query.lower():
    speak('Searching wikipedia.....')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    # webbrowser.open_new_tab("youtube.com")
    url= "youtube.com"

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open google' in query.lower():
    # webbrowser.open_new_tab("youtube.com")
    url= "google.com"

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\nguye\\Downloads\\music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} thr time is {strTime}")

elif 'open code' in query.lower():
    codePath = "C:\\Users\\nguye\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

elif 'email to potter' in query.lower():
    try:
        speak("what should I send")
        content = takeCommand()
        to = "dpbao.17it3@sict.udn.vn"
        sendEmail(to, content)
        speak("Email has been sent successfully")

    except Exception as e:
        print(e)

