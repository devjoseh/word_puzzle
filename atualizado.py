#Program: CSE 110 - W04 Prove - Word Puzzle
#Author: Bruno de Sousa Teixeira

import random

print("Welcome to the Word Puzzle Game!")
print("I have a secret word that you need to find out what it is!")
print("Uppercase letter = correct position")
print("Lowercase letter = exists, but not in the correct position\n")

secret_words = ("newsletter", "office", "garbage", "mortgage", "advice", "selfish", "happiness", "squirrel", "character", "jaguar", "apple", "computer", "giraffe", "airplane", "school")

secret_word = random.choice(secret_words)
guess_count = 0
hint = ["_"] * len(secret_word) 

print(f"Your hint is {" ".join(hint)} ({len(secret_word)} letters)")

while True:
    guess = input("What is your guess? ").lower()
  
    if(guess == "quit"):
        print("Thank you for playing with us. Bye! ")
        break
  
    if(len(guess) != len(secret_word)):
        print(f"Your guess must be {len(secret_word)} letters long. Try again")
        continue
  
    guess_count += 1 

    if secret_word == guess:
        print(f"Congratulations! The secret word was {secret_word}.")
        if guess_count == 1:
            print("You took just 1 guess! ")
        else:
            print(f"You took {guess_count} guesses. ")
        break
    else:
        print("Your guess was incorrect! ")

        for i, letter in enumerate(guess):
            if(guess[i] == secret_word[i]):
                hint[i] = letter.upper()
            elif letter in secret_word and guess[i] != secret_word[i]:
                if hint[i] != letter.upper():
                    hint[i] = letter.lower()

        print(f"Your hint is: {" ".join(hint)}")