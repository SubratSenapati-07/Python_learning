# Sr_alexa :


import speech_recognition as sr
import webbrowser 
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text) 
    engine.runAndWait()

def processCommand(c):
    pass
if __name__ == "__main__":
    speak("Initializing Alexa...")
    while True:
    # listen for the wake word "Alexa"
    # Obtain audio by microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source,phrase_time_limit=1)

        
        print("recongnizing...")
        # reconize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,phrase_time_limit=2)

            command = r.recognize_google(audio)
            print(command)
            if(command.lower() == "alexa"):
                speak("Yes!")
                # listen for command
                with sr.Microphone() as source:
                    print("Alexa Active...")
                    audio = r.listen(source)

                    processCommand()
        except Exception as e:
            print("Error; {0}".format(e))

