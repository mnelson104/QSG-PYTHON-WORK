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

for i in range(99,0,-1):
    if i == 1:
        print("1 bottle of beer on the wall. 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        continue
    else:
        print(str(i) + " bottles of beer on the wall. " + str(i) + "bottles of beer.")
        print("Take one down and pass it around, " + str(i-1) + " bottles of beer on the wall.\n")
print("No more bottles of beer on the wall!")
