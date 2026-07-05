class ATM:
    def __init__(self,pin):
        self.__pin = pin
    
    def get_pin(self):
        return self.__pin
my_atm = ATM(1234)
print(my_atm.get_pin())