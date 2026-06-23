score = 10 # global variable
def increase_score():
    # agar hme global variable ki value ko badalna h function ka andar to hum global keyword ka use karta h 
    global score
    score = score + 5

increase_score()
print(score)