from flask import Flask,render_template,redirect,request,url_for,jsonify
import pyttsx3
import speech_recognition as sr
import webbrowser



app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)  

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
        #return "None"
    return jsonify("Working")  
if __name__ == "__main__":
    app.run()
   