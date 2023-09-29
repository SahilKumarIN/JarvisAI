import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# engine.setProperty('rate' , 250)

# print(voices)

# function to convert the text into speech and play the speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the master as good morning , afternoon etc.. and special day wishes
def wishMe():
    hour = int(datetime.datetime.now().hour)
    date = str(datetime.date.today())
    print(date)
    if '12-25' in date:
        speak("Merry Christmas , Sir ")
    
    elif '01-01' in date:
        speak("Happy New Year , Sir")

    if hour>=0 and hour<12:
        speak("Good Morning , Sir")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon , Sir")
    
    else:
        speak("Good Evening , Sir ")
    
    speak("I am Jarvis your personal assistant . How may i help you")

# Function to take command from the user in audio format and convert it to text/string format
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said : {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "none"
    return query







if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences=2)
            speak("According to wikipedia , ")
            print(results)
            speak(results)
        
        elif 'your name' in query:
            speak("My Name is Jarvis , Sir")
        
        elif 'my name ' in query:
            speak("Sir , Your name is Sahil")

        elif 'my birthday' in query:
            speak("Sir , Your Birthday is on 8th June . ")

        elif 'wake up' in query:
            speak("Ready at your service Sir . How may i help you . ")

        elif 'open youtube' in query:
            speak("Opening youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'music' in query:
            music_dir = 'E:\\songs'
            songs = os.listdir(music_dir)
            speak("Playing Music..")
            os.startfile(os.path.join(music_dir , songs[0]))

        elif 'play my library' in query:
            speak("Playing your library Boss . ")
            webbrowser.open("https://youtu.be/qN-3aPyIovQ")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , The time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.date.today()
            speak(f"Sir , Today is {strDate}")
        
        elif 'thank you' in query:
            speak("It's my pleasure sir ")
        
        elif 'open code' in query:
            path = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening visual studio code")
            os.startfile(path)

        elif 'open chrome' in query:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("opening chrome")
            os.startfile(path)

        elif 'good night ' in query:
            speak("Good night Sir , Sweet  dreams. ")
        
        elif 'my details' in query:
            speak('Sir your name is Sahil Kumar. currently you are pursuing your B.tech degree from B.C.E.T durgapur . You are also the owner of programmersahil.com , programmersahil.in , krsahil.me etc.. you also have so man android apps as your project , thank you.')
        
        elif 'open my website' in query:
            speak("Opening your website sir")
            webbrowser.open("https://krsahil.me")

        elif 'search ' in query:
            query=query.replace('search' , "")
            speak(f"Searching on google for {query} ")
            search = "google.com/search?="+query
            print(search)
            webbrowser.open(search)
            
