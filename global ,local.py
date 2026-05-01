x = 4 # global variable

def my_function():
    global x
    x = 5
    y = 1 # local variable
    print(y)

my_function()
print(x)
