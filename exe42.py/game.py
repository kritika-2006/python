class GameCharacter:
    def __init__(self,name,health):
        self.name = name 
        self.health = health
    def check_status(self):
        if self.health > 0:
            print(f"{self.name} is still alive with {self.health} HP!")
        else:
            print(f"Game over! {self.name} has been defeated")

# objects
player1 = GameCharacter("IronMan",100)
player2 = GameCharacter("Thanos",0)
# calling
player1.check_status()
player2.check_status()