import pyttsx3
# import faulthandler; faulthandler.enable()

engine = pyttsx3.init()
engine.say("Hello you!")
engine.runAndWait()