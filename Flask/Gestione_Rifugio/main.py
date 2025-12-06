from Shelter import Shelter
from Cat import Cat
from Dog import Dog

# Creazione del rifugio
rifugio = Shelter(animals={}, adoptions={})

# Creazione degli animali
gatto = Cat(id="c1", name="Micio", age_years=3, weight_kg=4.5, indoor_only=True, favorite_toy="Pallina")
cane = Dog(id="d1", name="Fido", age_years=5, weight_kg=20.0, breed="Labrador", is_trained=True)

# Aggiunta degli animali al rifugio
rifugio.add(gatto)
rifugio.add(cane)

# Stampa informazioni sugli animali
print("Informazioni Gatto:")
print(gatto.info())
print("\nInformazioni Cane:")
print(cane.info())

# Controllo se un animale è adottato
print("\nIl gatto è adottato?", rifugio.is_adopted("C001"))

# Segna il gatto come adottato
rifugio.set_adopted("C001", "Mario Rossi")
print("Il gatto è adottato?", rifugio.is_adopted("C001"))