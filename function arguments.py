"""def average(a,b, c=1):
    print("The average is " , ((a+b+c)/3))

average(1,2,3) """
    
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
       sum = sum + i
    #print("Average is: ", sum / len(numbers))
    return sum / len(numbers)

c = average(5,6)
print(c)
