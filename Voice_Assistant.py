
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[-1].id)

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kjjsinghh@gmail.com','karanis01')
    server.sendmail('kjjsinghh@gmail.com',to,content)
    server.close()






def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        print("Good Morning")
        speak("Good Morning")

    elif hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon")


    else:
        print("Good Evening")
        speak("Good Evening")


    speak("Hey I am Kira, Your personal Virtual Voice Assistant.Please tell me how may I help you")
    print("Hey I am Kira, Your personal Virtual Voice Assistant.Please tell me how may I help you")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening :)....")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
    try:
        print("Recognizing....")
        query= r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Please say that again, Sir....")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    while True:
      query = takeCommand().lower()

      if 'in wikipedia' in query:
          speak('Searching Wikipedia...')
          query = query.replace("Wikipedia","")
          results = wikipedia.summary(query, sentences=1)
          speak("According to Wikipedia")
          print(results)
          speak(results)
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
      elif 'open facebook' in query:
          webbrowser.open("facebook.com")
      elif 'open supercell'  in query:
          webbrowser.open("www.supercell.com")
      elif 'play music' in query:
          mus_dir = 'D:\\audios'
          songs = os.listdir(mus_dir)
          print(songs)
          os.startfile(os.path.join(mus_dir,songs[0]))

      elif 'the time' in query:
          strtime = datetime.datetime.now().strftime("%H:%M:%S")
          print(f"The time is {strtime}")
          speak(f"The time is {strtime}")

      elif 'send email' in query:
          try:
              speak("What should i say?")
              content = takeCommand()
              to = "kjsingh@mitaoe.ac.in"
              sendEmail(to,content)
              print("Email has been sent")
              speak("Email has been sent")

          except Exception as e:
              print(e)
              speak("Sorry my friend Karan. I am not able to send this email")

      elif 'exit' in query:
          print("Bye sir, Stay Safe Stay Healthy.")
          speak("Bye sir, Stay Safe Stay Healthy.")

          break


