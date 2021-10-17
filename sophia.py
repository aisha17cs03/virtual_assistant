import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Aisha !")

    elif hour>=12 and hour<16:
        speak("Good Afternoon Aisha !")

    else:
        speak("Good Evening Aisha !")
    speak("I am Sophia. Please Tell me how may i help you")

def takeCommand():
    '''
    it take microphone input from the user and return string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening.")
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing....")
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again Please....")
        speak("Say that again Please....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    WishMe()
    while True: #program execute again and gain means its recognizing again and again"
    #if 1:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia. Please wait mam")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            '''It print the 2 sentance of wikipedia data that its search
            '''
            speak(results)
        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'email to your_friend' in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                to = "Your friends email id"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Aisha. I am not able to send this email")


        elif 'where you live' in query:
            speak("Your Heart Please check it")


        elif 'play music' in query:
            music_dir = 'This PC:\\Music\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open code' in query:
            codePath = "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)


        elif 'who is the boss' in query:
            speak("Aisha mam")

        elif 'hate me' in query:
            speak("NO, I donot")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam the time is {strTime}")

        elif 'love you' in query:
            speak("Love You Too") 

        elif 'your name' in query:
            speak("I am Sophia. Your's personal voice assistant")

       
        else:
            speak("Sorry I don't know")    

    