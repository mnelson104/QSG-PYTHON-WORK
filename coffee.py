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
#         "cups_sold": 16
#    },
#     {
#          "day": 2,
#          "coffe_inv": 84,
#          "advertising": "15",
#          "temp": 72,
#         "cups_sold": 20
#    },
#     {
#          "day": 3,
#          "coffe_inv": 64,
#          "advertising": "5",
#          "temp": 78,
#         "cups_sold": 10
#    },
# ]
# Create an empty sales list
sales = []

def welcome():
    print("ClydeBank Coffee Shop Simulator 4000, Version 1.00")
    print("Copyright (C) 2025 ClydeBank Media, All Rights Reserved.\n")
    print("Let's collect some infrmation before we start the game.\n")

def prompt(display = "Please input a string.", require = True):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s

def daily_stats(cash_on_hand,weather_temp,coffee_inventory):
                print("You have $" + str(cash_on_hand) + " cash on hand and the temperature is " + str(weather_temp) + " degrees.")
                print("You have enough coffee on hand to make " + str(coffee_inventory) + " cups of coffee.\n")

def convert_to_float(s):
     # If conversion fails, assign it to 0
    try:
        f = float(s)
    except ValueError:
        f = 0
    return f

def get_weather():
    # Generate a random temperature between 20 and 90 degrees
    # We will consider seasons later on, but this is good enough for now
    return randint(20, 90)

# Print welcome message
welcome()

# Get name and shop name
name = prompt("What is your name?",True)
shop_name = prompt("What do you want to name your coffee shop?",True)

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
    temperature = get_weather()

    # Display the cash and weather
    daily_stats(cash,temperature,coffee)

    # Get price of a cup of coffee
    cup_price = prompt("What do you want to charge per cup of coffee? ")

    # Get advertising budget
    print("\nYou can buy advertising to help promote sales.")
    advertising = prompt("How much advertising do you want to buy (0 for none)? ",False)

    # Convert advertising to float
    advertising = convert_to_float(advertising)

    # Deduct advertising from cash on hand
    cash -= advertising

    # TODO: Calculate today's performance
    # TODO: Display today's performance

    # Before we loop around, add a day
    day += 1