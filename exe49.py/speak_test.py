import pyttsx3  # 1. Toolbox ko import kiya
engine = pyttsx3.init() # 2. Speaking engine ko chalu (initialize) kiya
# 3. Jo aap bolwana chahti ho, woh yahan likho
engine.say("Hello kritika, your Python library learning as started successfully!")
# 4. Engine ko command do ki ab zoor se bolo!
engine.runAndWait()