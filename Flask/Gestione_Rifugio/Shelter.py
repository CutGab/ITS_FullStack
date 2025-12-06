# Classe Shelter
# La classe Shelter rappresenta il contenitore principale del sistema, che gestisce tutti gli animali presenti nel rifugio.

# Attributi
# animals: dizionario che associa a ogni identificativo (id) l’oggetto Animal corrispondente, ad esempio:

# { "d1": <Dog ...>, "c1": <Cat ...>, ... }
# adoptions (opzionale ma consigliato): struttura dati per gestire lo stato di adozione, ad esempio un dizionario:

# { "d1": "Mario Rossi", "c1": "Luca Bianchi" }
# dove la chiave è l’id dell’animale e il valore è il nome dell’adottante.

# Metodi

# add(animal): aggiunge un animale al rifugio.
# Se esiste già un animale con lo stesso id, puoi decidere se sovrascriverlo o ignorare l’operazione 
# (nel contesto dell’esercizio è sufficiente una scelta semplice e documentata nei commenti).

# get(animal_id): restituisce l’oggetto Animal corrispondente all’ID specificato oppure None se non esiste.

# list_all(): restituisce una lista di tutte le istanze di Animal presenti nel rifugio 
# (puoi decidere se restituire direttamente gli oggetti o piuttosto una lista di dizionari generati con info()).

# is_adopted(animal_id): restituisce True/False a seconda che l’animale risulti adottato nella struttura adoptions.

# set_adopted(animal_id, adopter_name): registra l’adozione per un dato animale, salvando il nome dell’adottante.

# Nel codice principale dovrà essere creato un rifugio e dovranno essere creati almeno due animali, 
# uno di tipo Dog e uno di tipo Cat, che saranno aggiunti al rifugio prima di avviare l’app Flask.

from Animal import Animal
from Cat import Cat
from Dog import Dog

class Shelter:

    def __init__(self, animals: dict[str, Animal], adoptions: dict[str, str]):
        self.animals = animals
        self.adoptions = adoptions

    def add(self, animal: Animal):
        if animal.id in self.animals:
            return "Errore, animale già nel rifugio."
        
        else: 
            self.animals[animal.id] = animal

    def get(self, animal_id: str):
        if animal_id in self.animals:
            return self.animals[animal_id]
        
        else:
            return None
        
    def list_all(self):

        animal_info = []

        for animal in self.animals.values():

            animal_info.append(animal.info())
            
        return animal_info

        
    def is_adopted(self, animal_id: str):
        if animal_id in self.adoptions:
            return True
        
        return False
    
    def set_adopted(self, animal_id: str, adopter_name: str):

        if animal_id not in self.adoptions:
            self.adoptions[animal_id] = adopter_name

        else:
            return "L'animale è già stato adottato"