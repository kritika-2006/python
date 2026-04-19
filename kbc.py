question =[
     ["Python kya hai?", "language", "fruit", 1],
     ["India ki capital?", "mumbai","Delhi", 2]
]

money =0
#loop jo har sawal ko dikhayaga
for q in question:
    print("\nSawal:", q[0])
    print("1.",q[1])
    print("2.",q[2])
    ans = int(input("Sahi option number dalein: (1 or 2):"))
    if ans == q[3]:
        print("Sahi ans!")
        money = money + 1000
    else:
        print("Galat ans! Game Over")
        break
print ("\nAapne kul $",money,"jeete!")