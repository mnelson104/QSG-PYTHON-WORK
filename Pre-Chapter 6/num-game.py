from random import seed
from random import randint
# Seed random number generator

number = randint(1,30)
guess_count = 0
guess = 0

print("Welcome to my very own number guessing game!")
print("I have selected a number between 1 and 30. Can you guess what it is?")
while guess != number:
    guess = int(input("Enter your guess: "))
    guess_count += 1
    if guess < number:
        print("Your guess is too low. Try again.")
    elif guess > number:
        print("Your guess is too high. Try again.")
    else:
        print("Congratulations! You guessed the number in " + str(guess_count) + " tries.")