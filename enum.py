marks = [1,4,5,12,98,56]
# normal 
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("kritika")
    index+=1
print("\n")
# enumerate
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("kritika") 
