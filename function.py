def calculateGmean(a, b): # function
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a,b):
    if(a<b):
        print("a is less than b ")
    else:
        print("b is less than or equal ")
a = 2
b = 4
isGreater(a,b)
isLesser(a,b)
calculateGmean(a,b)

c = 6
d = 8
isGreater(c,d)
isLesser(c,d)
calculateGmean(c,d)
