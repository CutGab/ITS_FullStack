# Classe Animal
# La classe Animal rappresenta un animale generico del rifugio.
# È una classe astratta e non può essere istanziata direttamente.

# Ogni animale ha:

# un identificativo id di tipo stringa (es. "d1", "c3"),

# un nome name di tipo stringa,

# un’età age_years di tipo intero (anni),

# un peso weight_kg di tipo float (chilogrammi).

# Metodi
# species(): metodo astratto.
# Deve essere implementato nelle sottoclassi per restituire la specie dell’animale, ad esempio "dog" o "cat".

# daily_food_grams(): metodo astratto.
# Deve essere implementato nelle sottoclassi e deve restituire la quantità di cibo giornaliera raccomandata in grammi.

# info(): metodo concreto.
# Restituisce un dizionario con le informazioni principali dell’animale, ad esempio:

# { "id": ..., "name": ..., "species": ..., "age_years": ..., "weight_kg": ..., # più eventuali campi specifici delle sottoclassi }
# bmi_like(): metodo concreto che restituisce un valore derivato (simile a un indice di “forma fisica”), ad esempio calcolato come:

# weight_kg / (age_years + 1)
# Il dettaglio della formula è lasciato libero, l’importante è che sia coerente e restituisca un numero (float).

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, id: str, name: str, age_years: int, weight_kg: float):
        self.id = id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg

    @abstractmethod
    def species():
        pass

    @abstractmethod
    def daily_food_grams():
        pass

    def info(self):
        return f'id: {self.id}\n name: {self.name}\n age_years: {self.age_years}\n weight_kg: {self.weight_kg}'
    
    def bmi_like(self):
        return self.weight_kg / (self.age_years + 1)