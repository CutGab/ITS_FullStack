from Park import Park
from Rollercoaster import Rollercoaster
from Carousel import Carousel

    # Creazione del parco con un dizionario vuoto di attrazioni
my_park = Park({})

# Creazione di una Rollercoaster
rc = Rollercoaster (
    id = "2",
    nome = "Dragon Fury",
    min_height_cm = 140,
    inversions = 3
)

# Creazione di una Carousel
carousel = Carousel (
    id = "1",
    nome = "Magic Horses",
    min_height_cm = 0,
    animali = ["Cavalli", "Unicorni", "Draghetti"]
)

# Aggiunta delle attrazioni al parco
my_park.add(rc)
my_park.add(carousel)

# Stampa delle informazioni di tutte le attrazioni
print("=== Lista Attrazioni nel Parco ===")

for ride in my_park.list_all():
    print(ride.info())