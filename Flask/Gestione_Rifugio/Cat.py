# Classe Cat
# La classe Cat rappresenta un gatto e eredita da Animal.

# Attributi aggiuntivi
# indoor_only: booleano che indica se il gatto vive solo in casa (True/False),

# favorite_toy: stringa che rappresenta il gioco preferito (es. "ball", "mouse").

# Metodi
# species(): restituisce la stringa "cat".

# daily_food_grams(): restituisce la quantità di cibo giornaliero in grammi.
# Anche qui puoi usare una formula plausibile, ad esempio:

# return 100 + age_years * 30
# info(): estende il metodo della superclasse includendo anche indoor_only e favorite_toy.

from Animal import Animal

class Cat(Animal):

    def __init__(self, id, name, age_years, weight_kg, indoor_only: bool, favorite_toy: str ):
        super().__init__(id, name, age_years, weight_kg)

        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy

    def species():
        return 'cat'
    
    def daily_food_grams(self):
        return (100 + self.age_years) * 30
    
    def info(self):
        return f'id: {self.id} name: {self.name} age_years: {self.age_years} weight_kg: {self.weight_kg} indoor_only: {self.indoor_only} favorite_toy: {self.favorite_toy}'