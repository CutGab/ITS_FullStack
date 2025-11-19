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