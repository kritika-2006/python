try:
    a = int(input("first nuum:"))
    b = int(input("second num:"))
    print("Result:",a/b)

except ZeroDivisionError:
    print("Don't divide by zero")
except ValueError:
    print("only numbers are allowed")

