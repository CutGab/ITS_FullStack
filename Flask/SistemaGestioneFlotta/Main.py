# driver.py
from FleetManager import FleetManager
from Car import Car
from Van import Van

car1 = Car("AB123CD", "Fiat 500", "Mario Rossi", 2018, "Disponibile", doors=3, is_cabrio=False)
car2 = Car("EF456GH", "BMW Z4", "Laura Bianchi", 2022, "Manutenzione", doors=2, is_cabrio=True)

van1 = Van("XY789ZT", "Ford Transit", "Luca Verdi", 2020, "Disponibile", max_load_kg=1200, require_special_license=True)

# Creo un FleetManager con un dizionario iniziale
fm = FleetManager({
    car1.plate_id: car1,
    van1.plate_id: van1
    })

# Aggiungo un veicolo
fm.add(car2)

# Stampo tutti i veicoli
print("\n--- LISTA FLOTTA ---")
fm.list_all()

# Recupero un veicolo
print("\n--- RECUPERO VEICOLO 'EF456GH' ---")
v = fm.get("EF456GH")
if v:
    print(v.info())

# Cancello un veicolo
print("\n--- DELETE 'AB123CD' ---")
fm.delete("AB123CD")
fm.list_all()
