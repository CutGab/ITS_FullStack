# Classe Dog
# La classe Dog rappresenta un cane e eredita da Animal.

# Attributi aggiuntivi
# breed: razza del cane, stringa (es. "labrador"),

# is_trained: booleano che indica se il cane è addestrato (True/False).

# Metodi
# species(): restituisce la stringa "dog".

# daily_food_grams(): restituisce la quantità di cibo giornaliero in grammi.
# Puoi usare una formula plausibile, ad esempio:

# return 200 + age_years * 50
# oppure un’altra a tua scelta, purché sia chiaro che il risultato rappresenta grammi di cibo al giorno.

# info(): estende il metodo della superclasse includendo anche breed e is_trained.

from Animal import Animal

class Dog(Animal):

    def __init__(self, id, name, age_years, weight_kg, breed: str, is_trained: bool):
        super().__init__(id, name, age_years, weight_kg)

        self.breed = breed
        self.is_trained = is_trained

    def species(self):
        return "dog"
    
    def daily_food_grams(self):
        return (200 + self.age_years) * 50
    
    def info(self):
        return f'id: {self.id} name: {self.name} age_years: {self.age_years} weight_kg: {self.weight_kg} breed: {self.breed} is_trained: {self.is_trained}'