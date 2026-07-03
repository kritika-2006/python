class camera:
    def take_photo(self):
        print("Click! Photo taken.")
class musicPlayer:
    def play_music(self):
        print("Playing songs...")
class SmartPhone(camera,musicPlayer):
    pass
sp = SmartPhone()
sp.take_photo()
sp.play_music()
