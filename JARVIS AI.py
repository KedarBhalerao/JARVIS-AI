import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import smtplib 
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newvoicesrates = 150
engine.setProperty('rate',newvoicesrates)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Hello!Welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 15:
        speak("Good Afternoon")
    else:
        speak("Good Evening")        
    speak("Ragnar at service. How can i help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:

        print(e)

        speak('Say that again please...')
        return 'None'
    
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("kedarbhalerao366@gmail.com","kedar123@")
    server.sendmail("kedarbhalerao366@gmail.com",to, content)
    server.close()

def screenshot():

    img = pyautogui.screenshot()
    img.save("D:\screenshots project\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("Cpu is at "+ usage)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)


        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak("searching")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)  

        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "kedarbhalerao366@gmail.com"
                #sendmail(to,content)
                speak("email sent sucessfully")

            except Exception as e:
                speak(e)
                speak("unable to send mail")

        elif "search in chrome" in query:
            speak("What should i search for?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown - /s /t 1")

        elif "restart" in query:
            os.system("shutdown -  /r /t 1")

        elif "play songs" in query:
            songs_dir = "D:\songs"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "take screenshot" in query:
            screenshot()
            speak("screenshot taken")

        elif "cpu" in query:
            cpu()

        elif "tell me joke" in query:
            jokes()

        elif "offline" in query:
            speak("Going offline! Goodbye Sir!")
            quit()    



