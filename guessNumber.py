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

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback !='c' :
        if low!=high :
         guess=random.randint(low,high)
        else :
            guess=high    
        feedback=input(f" is {guess} to high(H) , to low(L) or correct (C)  : ").lower()
        if feedback=="h":
            high=guess-1
        elif feedback=='l':
            low=guess+1    
    print(f" Yay ! Compute guessed your number , {guess}, correctly ")
    
computer_guess(20)            