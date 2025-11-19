# 9-1. Restaurant: Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: list):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}")


    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")



Res1 = Restaurant ("Day Vito", ["Italiana", "Cinese"])

print(Res1.restaurant_name)
print(Res1.cuisine_type)

print("")

print("*" * 10)

print("")

Res1.describe_restaurant()
print("")
Res1.open_restaurant()

print("")

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

Res2 = Restaurant ("Wong San", ["Giapponese", "Cinese"])
Res3 = Restaurant ("UKing", ["Inglese"])
Res4 = Restaurant ("Burger King", ["Fast Food"])

Res2.describe_restaurant()
print("*" * 10)
Res3.describe_restaurant()
print("*" * 10)
Res4.describe_restaurant()