# 8-14. Cars: Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
# Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 

def build_car(manufacturer: str, mode_name: str, **kwargs):
    
    car: dict = {
        "Manufacturer": manufacturer,
        "Model Name": mode_name
    }

    if kwargs:

        car.update(kwargs)

    for key, values in car.items():
        print(f"{key}: {values}")

build_car("Subaru", "Outback", color="Blue", Tow_package=True)

