x = 4
print(x)

def hello():
    x = 5
    y = 1
    print(f"The local x is {x}")
    print("Hello kritika")

print(f"The global x is {x}")
hello()
x = 5
print(f"The global x is {x}")
