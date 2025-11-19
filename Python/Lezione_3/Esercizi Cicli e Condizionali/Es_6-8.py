# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet. 

Pet_1: dict = {"Name": "Simba",
                "Type": "Lion",
                "Owner": "Mark"}

Pet_2: dict = {"Name": "Perry",
                "Type": "Ornitorinco",
                "Owner": "Candice"}

Pet_3: dict = {"Name": "Minou",
                "Type": "Cat",
                "Owner": "Lion"}

pets: list = [Pet_1, Pet_2, Pet_3]

print("")

for i in pets:
    print(i)