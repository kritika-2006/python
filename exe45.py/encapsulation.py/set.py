class ATM:
    def __init__(self, pin):
        self.__pin = pin

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if len(str(new_pin)) == 4:
            self.__pin = new_pin
            print("Pin updated succesfully!")
        else:
            print("Error : Pin must be exactly 4 digits")
my_atm= ATM(1234)
my_atm.set_pin(5545)
print("Current Pin is:",my_atm.get_pin())