fname = input("what is your first name?")
print("The first letter of your name is " + fname[0])

# This is an example of a list
# Lists are mutable, meaning they can be changed
grocery_list = ["eggs", "milk", "cheese", "pasta"]
print("The first item on your grocery list is " + grocery_list[0])
print("The last item on your grocery list is " + grocery_list[-1])

# This is an example of a tuple
# Tuples are immutable, meaning they cannot be changed
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
print("The third planet from the sun is ... " + planets[3])

## This is an example of a set
# Sets are unordered collections of unique items
customers = {
    "James Smith", 
    "Andrea Richards", 
    "Sam Sharp", 
    "Brenda Longmire", 
    "Veronica Marsh", 
    "Sylvia Smith", 
    "James Smith", 
    "Venesa Bush", 
    "Steve Hammersmith", 
    "Brenda Longmire", 
    "Sylvia Smith", 
    "Steve Hammersmith", 
    "Walt Hawkins"}
print(customers)

# This is an example of a dictionary
# Dictionaries are collections of key-value pairs
customer1 = {
    "name": "James Smith",
    "age": 24,
    "phone": "555-555-1941",
    "email": "james@xyzinternet.com"
}
customer2 = {
    "name": "Andrea Richards",
    "age": 33,
    "phone": "555-555-4928",
    "email": "andrea@coffeeloversunite.us"
}
print(customer1["name"])

# This is an example of a for loop using a range
# From chapter 3
for i in range(99,0,-1):
    if i == 1:
        print("1 bottle of beer on the wall. 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        continue
    else:
        print(str(i) + " bottles of beer on the wall. " + str(i) + "bottles of beer.")
        print("Take one down and pass it around, " + str(i-1) + " bottles of beer on the wall.\n")
print("No more bottles of beer on the wall!")

# This is an example of error handling from chapter 4

# Divide a number by zero

a = 7
b = 0

try:
    print(str(a) + " divided by " + str(b) + " is " + str(a/b))
except Exception as e:
    print("Sorry a problem occured dividing the numbers.")
    print("Error details: " + str(e))
finally:
    print("But still we tried")
print("Finally, we are done!")

# Testing a toktok video i saw with comments turned off
x = [1, 2, 3]
print(max(x))

# Chapter 5 stuff

# Define the ask function
def ask(prompt):
    return input(prompt + " ")

# Use the ask function to find out how many cups we want
# Can be simplified by placing the ask in the print instead of a new variable
question = ask("How many cups do you want?") 
print(question)

# Refactoring ther 99 bottles code with a generator function
def bottles_song(start = 99):
    # Set the initial number of bottles to the start argument
    bottles = start
    # Loop through until bottles are gone
    while bottles > 0:
        # display the song
        print(str(bottles) + " bottles of beer on the wall.")
        print(str(bottles) + " bottles of beer.")
        print("Take one down and pass it around, ")
        # subtract one bottle
        bottles -= 1
        print(str(bottles) + " bottles of beer on the wall.")
        # Yield to the calling function
        yield
        # Pick back up here when we return
    return True

# Loop through the generator
for i in bottles_song(5):
    # Don't do anything as the generator does the printing
    pass

#Defint the bottle_song_new function with the start argument defaulting to 99
def bottles_song_new(start = 99):
    # Set the initial number of bottles to the start argument
    bottles = start
    # loop through until bottles are gone
    while bottles > 0:
        # display the song
        this_verse = []
        this_verse.append(str(bottles) + " bottles of beer on the wall. \n")
        this_verse.append(str(bottles) + " bottles of beer. \n")
        this_verse.append("Take one down and pass it around, ")
        # subtract one bottle
        bottles -= 1
        this_verse.append(str(bottles) + " bottles of beer on the wall. \n")
        # Yield to the calling function
        yield "".join(this_verse)
        # Pick back up here when we return
    return True

# Loop through the generator
for v in bottles_song_new():
    print(v)

#Defint the bottle_song_new function with the start argument defaulting to 1 and counting up
def bottles_song_new(start = 0):
    # Set the initial number of bottles to the start argument
    bottles = start
    # loop through until bottles are gone
    while bottles < 99:
        # display the song
        this_verse = []
        this_verse.append(str(bottles) + " bottles of beer on the wall. \n")
        this_verse.append(str(bottles) + " bottles of beer. \n")
        this_verse.append("Take one out and place it about, ")
        # add one bottle
        bottles += 1
        this_verse.append(str(bottles) + " bottles of beer on the wall. \n")
        # Yield to the calling function
        yield "".join(this_verse)
        # Pick back up here when we return
    return True

# Loop through the generator
for v in bottles_song_new():
    print(v)