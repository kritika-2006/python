a = int(input("Enter any value between 5 and 9:"))
# user khud error lata h taki program half ma he error dikhada
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")