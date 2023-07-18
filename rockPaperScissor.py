import random


def play():
    user = input(
         " what is yourj choice? enter 's' for scissor , 'r' for rock , 'p' for paper : \n").lower()
    computer = random.choice(['r', 'p', "s"])
  
    
    
    if user ==computer :
        return " It is tie"
    if is_win(user,computer):
        return "You have won"
    return "you lost"
    
    
def is_win(player,opponent):
    if(player=="r" and opponent=="s") or (player=="s" and opponent=="p") or (player=="p" and opponent=="rock"):
        return True  


print(play())
