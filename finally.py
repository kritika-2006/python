# in function when some error are occured then always finally statement is print
def func1():
 try:
    l = [1,2,3,4,5]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
 except:
    print("Some error occured")
    return 0

 finally:
    print("I am always executed")

x = func1()
print(x)