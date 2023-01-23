# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 1/23/2023
# Description: Prompts user for an integer that the player will try to guess. Tells user if integer
#              is too high, too low, or guessed correctly and outputs number of tries it took.
num_guess = 1
guess = 0
print("Enter the integer for the player to guess.")
answer = int(input())
print("Enter your guess.")
guess = int(input())
if guess == answer:
    print("You guessed it in 1 try.")
while guess != answer:
    if guess > answer:
        print("Too high - try again:")
    if guess < answer:
        print("Too low - try again:")
    num_guess += 1
    guess = int(input())
if guess == answer:
    print("You guessed it in", num_guess, "tries.")