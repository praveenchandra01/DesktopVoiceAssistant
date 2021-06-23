import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    h = int(datetime.datetime.now().hour)
    if h >= 0 and h < 12:
        speak("Good Morning!")
    elif h >= 12 and h <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I am Xemp. Please tell me how may i help you")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening....")
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said : {query}")
            speak(query)
        except Exception:
            # speak("Say that again please")
            return 'None'
        return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("praveenchandra273v@gmail.com", "<password>")
    server.sendmail("praveenchandra273v@gmail.com", to, content)
    server.close()


if __name__ == '__main__':
    speak("Opening..")
    greet()
    # while True:
    for i in range(2):
        query = listen().lower()

        if 'time' in query:
            st = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak(f"Sir the time is {st}")
            

        elif 'search on wikipedia about' in query:
            speak('Serching wikipedia...')
            try:
                query = query.replace("search on wikipedia about", "")
                res = wikipedia.summary(query, sentences=2)
                print(res)
                speak('according to wikipedia' + res)
            except Exception as e:
                speak('Sorry sir, unable to get infomation')
            break


        elif 'play music' in query:
            music_dir = 'F:\\SONGS\\English'
            songs = os.listdir(music_dir)
            a = random.randint(0, 164)
            os.startfile(os.path.join(music_dir, songs[a]))
            break


        elif 'open vs code' in query:
            path = "C:\\Users\\PRAVEEN Chandra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            break


        elif 'open spotify' in query:
            path = "C:\\Users\\PRAVEEN Chandra\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(path)
            break


        elif 'open youtube' in query:
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                           ).open('youtube.com')
            break


        elif 'play lo-fi music' in query:
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                           ).open('https://www.youtube.com/watch?v=tgY1b0AX7B8&ab_channel=AudioFurix')
            break


        elif 'play lofi music' in query:
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                           ).open('https://www.youtube.com/watch?v=tgY1b0AX7B8&ab_channel=AudioFurix')
            break


        elif 'open google' in query:
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                           ).open('google.com')
            break


        elif 'open stack overflow' in query:
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                           ).open('https://stackoverflow.com/')
            break


        elif 'search' in query:
            speak("What do you want to search")
            search = listen()
            search=search.replace("about","")
            url = "https://google.com/search?q=" + search
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                           ).open(url)
            break


        elif 'find location' in query:
            speak("Name the location")
            loc = listen()
            url = "https://google.nl/maps/place/" + loc + '/&amp;'
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                           ).open(url)
            break


        elif 'send email' in query:
            try:
                speak("Please tell me the content of your email")
                content = listen()
                to = ""
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception:
                speak("Sorry sir unable to send email")
            break


        elif 'quit program' in query:
            speak("Quitting sir, Thankyou for your time")
            exit()


        elif 'exit program' in query:
            speak("Thankyou for your time")
            exit()

        else:
            # print("sorry")
            speak("Sorry sir i didn't get that please repeat")
