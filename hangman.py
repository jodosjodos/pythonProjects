import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word



def hangman():

    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives=6
    while len(word_letters) > 0 and lives > 0:
        print(f" you remain wiht {lives} lives and  You have used these lettes : "," ".join(used_letters))
        word_list=[letter if letter in used_letters else "-" for letter in word]
        print("Current word : ", " ".join(word_list))
        user_input = input(" Guess a letter : ").upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else :
                lives -=1    
        elif user_input in used_letters:
            print(" You have already used that character ! please try another character")
        else:
            print("Invalid character . please try  again")
    if lives==0:
        print(f"soryy you have died , the word was {word} ")
    else :
        print(f"You have guessed  the word {word} !!! ")
            

hangman()
