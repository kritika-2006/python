import pyttsx3
import requests
import os

engine = pyttsx3.init()
engine.setProperty('rate',120)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("welcome kritika,please select an option.")
engine.runAndWait()

target_url = "https://google.com"

while True:
    print("\n-- Menu --")
    print( "1. check website status")
    print(  "2. create folder")
    print(  "3. exit" )
    choice = input("Enter option (1-3):")
    if choice == "1":
       try:
          response = requests.get(target_url)
          if response.status_code == 200:
             print("Website sahi chal rhi h!")
          else:
            print("There is an error")
       except:
          print("kuch gadbad h ya internet band h ")
    
    elif choice == "2":
       folder_name = input("put the name of the first folder:")
       if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print("📁 folder ban gya!")
       else:
            print("⚠️ Folder already exists!")

    elif choice == "3":
       engine.say("goodbye")
       engine.runAndWait()
       print("Assistant turned off. Bye!")
       break
    else:
      print("invalid choice")

