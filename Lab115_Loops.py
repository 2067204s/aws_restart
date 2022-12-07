#Working with Loops : while loop, for loop

# Exercise 1: Working with a while loop

import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)   #will generate a random number between 1 and 10
isGuessRight = False
while isGuessRight != True:     #to handle the game logic, create a while loop:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
