class Account:
    def __init__(self, owner, balance):
        self.owner = owner # Pubic
        self.__balance = balance  # Private

a1 = Account("Kritika", 50000)

print(a1.owner)
print(a1.__balance) # error ayega because balance private h and usko class ka bahar call karenge toh print nhi hoga


