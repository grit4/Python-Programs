import random
def roll():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print(" ",dice1,"    ",dice2)
    return dice1+dice2
    
def crap():
    print("Dice1  Dice2")
    sum=roll()
    if sum in [2,3,12]:
        return "LOSE"
    elif sum in [7,11]:
        return "WIN"
    while True:
        s=roll()
        if s==sum:
            return "WIN"
        elif s==7:
            return "LOSE"
         
print("You",crap())