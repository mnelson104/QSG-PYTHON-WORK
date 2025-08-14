# ClydeBank Coffee Shop Simulator 4000
# Copyright (C) 2025  ClydeBank Media, All Rights Reserved
#import items from the random module to generate weather
from random import seed
from random import randint

# Current day number
day = 1

#Starting cash on hand
cash = 100.00

#Coffee on hand (cups)
coffee = 100

# Sales list of dictionaries
# sales = [
#     {
#          "day": 1,
#          "coffe_inv": 100,
#          "advertising": "10",
#          "temp": 68,
#         "cups_siold": 16
#    },
#     {
#          "day": 2,
#          "coffe_inv": 84,
#          "advertising": "15",
#          "temp": 72,
#         "cups_siold": 20
#    },
#     {
#          "day": 3,
#          "coffe_inv": 64,
#          "advertising": "5",
#          "temp": 78,
#         "cups_siold": 10
#    },
# ]
# Create an empty sales list
sales = []

# Print the welcome message
print("ClydeBank Coffee Shop Simulator 4000, Version 1.00")
print("Copyright (C) 2025 ClydeBank Media, All Rights Reserved.\n")
print("Let's collect some infrmation before we start the game.\n")

# Get name and shop name by using the following approach
# 1. Set name and shop_name to False
# 2. Use while not name nd shop_name to continue to promt for a non-empty string
name = False
while not name:
    name = input("What is your name? ")

shop_name = False
while not shop_name:
    shop_name = input("What do you want to name your coffee shop? ")

# We have what we need, let's get started!

#print("\nThanks, " + name + ". Let's set some initial pricing.\n")
#
#
# Display what we have
#print("\nGreat. Here's what we've collected so far.\n")
#print("Your name is " + name + " and you're opening " + shop_name + ".")
#print("Your first cup of coffee will sell for $" + cup_price + ".\n")

print("\nOK, let's get started!. Have fun!")

#The main game loop

running = True
while running:
    # Display the day and add a "fancy" text effect
    print("\n-----| Day " + str(day) + " @" + shop_name + " |-----")

    # Generate a random temperature between 20 and 90 degrees
    # We will consider seasons later on, but this is good enough for now
    temperature = randint(20, 90)

    # Display the cash and weather
    print("You have $" + str(cash) + " cash and it's " + str(temperature) + " degrees.")
    print("You have enough coffe to make " + str(coffee) + " cups.\n")

    # Get price of a cup of coffee
    cup_price = input("What do you want to charge per cup of coffee? ")

    # Get advertising budget
    print("\nYou can buy advertising to help promote sales.")
    advertising = input("How much advertising do you want to buy (0 for none)? ")

    # Convert advertising to float
    # If it fails, set it to 0
    try:
        advertising = float(advertising)
    except ValueError:
        advertising = 0

    # Deduct advertising from cash on hand
    cash -= advertising

    # TODO: Calculate today's performance
    # TODO: Display today's performance

    # Before we loop around, add a day
    day += 1