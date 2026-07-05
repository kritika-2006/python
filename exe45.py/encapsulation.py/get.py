class ATM:
    def __init__(self,pin):
        self.__pin = pin
    
    # getter method :Iske jariye hum pin ko safe tareeke se bahar bhejenge
    def get_pin(self):  
        return self.__pin
    
    # Setter Method: Iske jariye hum badalne se pehle check kar sakte hain
    def set_pin(self,new_pin):
        self.__pin = new_pin
