import pyttsx3
engine = pyttsx3.init()
a = str(input("Enter any text here:"))
engine.say(a)
engine.runAndWait()