# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

cities: dict = {"Rome": {"Country": "Italy", "Population": 4000000, "Fact": "Cats are legally allowed to roam freely among the ruins — including the Colosseum!"},
                "Tokyo" : {"Country": "Japan", "Population": 10000000, "Fact": "There's a café where you can cuddle hedgehogs while sipping your drink."},
                "London" : {"Country": "UK", "Population": 3000000, "Fact": "Big Ben isn't the clock or the tower — it's actually the bell inside."}
}

for key, items in cities.items():
    print(f"{key}\n{items}")
    print()

