try:
    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution complete.")