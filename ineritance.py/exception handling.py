try:
    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
    # finally always execute either exception may be or may not
finally:
    print("Execution complete.")
