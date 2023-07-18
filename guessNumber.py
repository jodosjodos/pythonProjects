import random

def guess(x):
    random_number=random.randint(1,x)
    guessNumber=0
    while guessNumber != random_number :
        guessNumber=int(input(f"gues an number u want  btn 1 and  {x}  : "))
        if guessNumber < random_number :
            print("Soryy, guess again . to low")
        elif guessNumber > random_number :
            print("sorry, guess again . to high")    
    print(f"Yay , congratss . You have guessed the random Number correctly  {random_number}")


guess(20)