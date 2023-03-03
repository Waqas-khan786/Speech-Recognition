from flask import Flask,render_template,redirect,request,url_for,jsonify
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os
import smtplib


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

@app.route('/takeCommand',methods = ['POST'])
def takeCommand():
    #It takes microphone input from the user and returns string output
    userVoice = request.form['userVoice']
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        # _query = r.recognize_google(audio, language='en-in')
        _query = userVoice
        print(f"User said: {_query}\n")
        while True:
            #query = takeCommand().lower()
            query = _query.lower()
            print(query)
        # Logic for executing tasks based on query
            if 'open yahoo' in query or 'yahoo' in query:
                #speak('Searching yahoo...')
                # query = query.replace("yahoo", "")
                print("inside yahoo scope")
                webbrowser.open("yahoo.com")
                break

            elif 'open youtube' in query or 'youtube' in query:
                webbrowser.open("youtube.com")
                break

            elif 'open google' in query or 'google' in query:
                print("google working")
                webbrowser.open("google.com")
                break

            elif 'open stack overflow' in query or 'stack overflow' in query:
                print("inside stackoverflow scope")
                webbrowser.open("stackoverflow.com")
                break

            elif 'open facebook' in query or 'facebook' in query:
                print("inside facebook scope")
                webbrowser.open("facebook.com")
                break

            break

    except Exception as e:
        print(e)    
        print("Say that again please...")
        speak('Say that again please...')
        #return "None"
    return jsonify("Working")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


    wishMe()
    # while True:
    # # if 1:
    #     query = takeCommand().lower()

    #     # Logic for executing tasks based on query
    #     if 'yahoo' in query or 'open yahoo' in query:
    #         speak('Searching yahoo...')
    #         query = query.replace("yahoo", "")
    #         # results = wikipedia.summary(query, sentences=2)
    #         webbrowser.open("yahoo.com")
    #         # speak("According to Wikipedia")
    #         # print(results)
    #         # speak(results)

    #     elif 'open youtube' in query or 'youtube' in query:
    #         webbrowser.open("youtube.com")

    #     elif 'open google' in query or 'google' in query:
    #         webbrowser.open("google.com")

    #     elif 'open stackoverflow' in query:
    #         webbrowser.open("stackoverflow.com")   


        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0]))

        # elif 'the time' in query:
        #     strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        #     speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)

        # elif 'email to harry' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "harryyourEmail@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend harry bhai. I am not able to send this email")
if __name__ == "__main__":
    app.run()
   