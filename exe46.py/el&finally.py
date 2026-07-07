try:
    num = int(input("Enter number:"))
except ValueError:
    print("Error hua")
else:
    print("Wah! koi error nhi aya")
finally:
    print("Main toh hamesha chaluga , chahe jo ho jaye !")