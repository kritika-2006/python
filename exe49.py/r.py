import pyttsx3
engine = pyttsx3.init()
# Speed check karne ke liye:
speed = engine.getProperty('rate') # Purani speed nikaali
engine.setProperty('rate',150) # Nayi speed 150 set kar di (thoda slow aur saaf)
engine.say("I am speaking slowly now")
engine.runAndWait()