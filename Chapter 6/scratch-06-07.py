# Define a new class
class Customer:
    def __init__ (self,name, city):
        self.name = name
        self.city = city

    def __enter__ (self):
        print("Entering scope." )
        # Run code upon entering scope of with statement
        return self
    
    def __exit__ (self, exc_type, exc_value, traceback):
        print("Leaving scope." )
        # Run code upon exiting scope of with statement

    def greet(self):
        print ("Hello " + self.name + "!")

# Use with to create a scope
with Customer("Matthew", "Mays Landing") as matthew:
    matthew.greet()
