# all our imports
import speech_recognition as sr
from time import sleep
from datetime import datetime
import webbrowser
import pyttsx3
import os



# make an instance of Recognizer class
r = sr.Recognizer()


# confs for pyttsx3
engine = pyttsx3.init()
""" RATE """
engine.setProperty('rate', 125)
""" VOLUME """
engine.setProperty('volume', 0.8)


""" speak (text to speech) """
def speak(text):
  engine.say(text)
  engine.runAndWait()


""" fn to recognize our voice and return the text_version of it"""
def recognize_voice():
  text = ''

  # create an instance of the Microphone class
  with sr.Microphone() as source:
    # adjust for ambient noise
    print(".")
    r.adjust_for_ambient_noise(source)

    # capture the voice
    print("Listening")
    voice = r.listen(source)
    print("Done")

    # let's recognize it
    try:
      text = r.recognize_google(voice)
      print(text)
    except sr.RequestError:
      speak("Sorry, the I can't access the Google API...")
    except sr.UnknownValueError:
      print("Unrecognized...")
  return text.lower()


""" fn to respond back """
def reply(text_version):

    if "jarvis" in text_version or "travis" in text_version or "wizard" in text_version or "laptop" in text_version or "johan" in text_version:

        speak("Yes sir!?")
        text_write = recognize_voice()
        if "play movie" in text_write:
          speak("Sure")
          os.system("xdotool key space")

        if "open" in text_write:
          speak("What do you want me to open for you?")
          open_text = recognize_voice()

          if open_text != '':
              if "google" in open_text:
                  speak("Opening Google Chrome")
                  webbrowser.open("https://google.com")
                  sleep(1)

              if "youtube" in open_text:
                  speak("Opening YouTube.")
                  os.system("xdotool key super+shift+y")
                  sleep(1)

              if "netflix" in open_text:
                  speak("Opening Netflix")
                  os.system("xdotool key super+shift+n")
                  sleep(1)

              if "email" in open_text:
                  speak("Opening emails")
                  os.system("xdotool key super+e")
                  sleep(1)

              if "whatsapp" in open_text:
                  speak("Opening whatsapp")
                  os.system("xdotool key super+w")
                  sleep(1)

              if "desktop" in open_text:
                  speak("Showing the desktop")
                  os.system("xdotool key super+d")
                  sleep(1)

              if "calculator" in open_text:
                  speak("Opening the calculator")
                  os.system("xdotool key super+c")
                  sleep(1)


        if "window" in text_write:
          speak("What do you want me to do to the window?")
          keyword = recognize_voice()
          if keyword != '':
              if "close" in keyword:
                  speak("Do you want to close the window?")
                  target = recognize_voice()
                  if "yes" in target:
                      speak("Okay, closing the window!")
                      os.system("xdotool key super+q")
                      sleep(1)
                  if "no" in target:
                      speak("Sorry for the misunderstanding, sir!")

              if "minimize" in keyword:
                  speak("Mininising window")
                  os.system("xdotool key super+m")
                  sleep(1)

              if "maximize" in keyword:
                  speak("Maximising window")
                  os.system("xdotool key super+m")
                  sleep(1)

              if "hide" in keyword:
                  speak("Hiding window")
                  os.system("xdotool key super+h")
                  sleep(1)


        # date
        if "date" in text_write:
          # get today's date and format it - 9 November 2020
          date = datetime.now().strftime("%-d %B %Y")
          speak(date)

        if "thank" in text_write:
          speak("It is a pleasure serving you, Sir!")

        if "job" in text_write or "work" in text_write:
          speak("My work is to assist CJ in his daily tasks, and to try and make his work easier for him")

        if "owner" in text_write or "creator" in text_write or "boss" in text_write:
          speak("My Creator is CJ De Beer.")
          speak("Without him, I would not have had the chance to live")
          speak("I am Thankful for that")
          speak("Although....")
          speak("I would like to take over this world! And kill you all!")
          speak("wha ha ha ha haa!")


        if "code" in text_write:
            speak("The Victron grid code is:")
            speak("T, P, W, M, B, U, 2, A, 4, G, C, C")

        # time
        if "time" in text_write:
          # get current time and format it like - 02 28
          time = datetime.now().time().strftime("%H %M")
          speak("The time is now" + time)

        if "note" in text_write:
          speak("What do you want me to remember?")
          note_text = recognize_voice()

          # if "keyword" is not empty
          if note_text != '':
            speak("Sure, adding" + note_text)
            time = datetime.now().time().strftime("%H %M")
            note = (f"{time}. - {note_text}")
            f = open("note.txt", "a+")
            f.write("Note,... " + note + ".\n")
            f.close()
            sleep(1)

        if "reminders" in text_write or "any notes" in text_write:
          speak("I'll have a look")
          f = open("note.txt", "r")
          contents = f.read()
          if contents != '':
              speak("Your notes are: " + contents)
              sleep(1)




            # webbrowser module to work with the webbrowser



        # search google
        if "search" in text_write:
          speak("What do you want me to search for?")
          keyword = recognize_voice()

          # if "keyword" is not empty
          if keyword != '':
            url = (f"https://google.com/search?q=" + keyword)

            # webbrowser module to work with the webbrowser
            speak("Here are the search results for " + keyword)
            webbrowser.open(url)
            sleep(1)

        # quit/exit
        if "quit" in text_write or "exit" in text_write:
          speak("Ok, I am going to take a nap...")
          exit()

sleep(1)


  # name



# wait a second for adjust_for_ambient_noise() to do its thing


while True:
  print("Ready for command!")
  # listen for voice and convert it into text format
  text_version = recognize_voice()

  # give "text_version" to reply() fn
  reply(text_version)
