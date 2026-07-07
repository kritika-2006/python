try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    print("Result:",a/b)
except ZeroDivisionError:
    print("Any number is not divided by zero.")
except ValueError:
    print("Please enter only numbers not string.")
except Exception as e:
    print("undefined error.")
    