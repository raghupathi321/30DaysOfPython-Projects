import random
def NumberGuessing(x):
    number=random.randint(1,100)
    if x==number:
        return "You guessed it!"
    elif x<number:
        return "Too low!"
    elif x>number:
        return "Too high!"
    else:
        return "Invalid input!"


count=0
while count<5:
    x=int(input("Guess a number between 1 and 100: "))
    print(NumberGuessing(x))
    count=count+1
print("Game Over!")
    

    