import pyttsx3
engine = pyttsx3.init()
# speed set
engine.setProperty('rate',120)
# saari available voices nikalo
voices = engine.getProperty('voices')
# male voice ka liya use hota h (voices[0])
# Female voice set karo (voices[1] use karke)
engine.setProperty('voice',voices[1].id)
# speak
engine.say("Hello kriika, this is your new python assitant speaking...")
engine.runAndWait()
