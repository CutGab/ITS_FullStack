
# 9-4. Number Served: Start with your program from Exercise 9-1. 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then change this value and print it again. 
# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: list, number_served = 0):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}")


    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served

    def increment_number_served(self, increment: int):
        self.number_served += increment


Res1 = Restaurant ("Day Vito", ["Italiana", "Cinese"], 10)

print(Res1.number_served)

Res1.number_served = 20

print(Res1.number_served)

Res1.set_number_served(40)

print(Res1.number_served)

Res1.increment_number_served(10)

print(Res1.number_served)