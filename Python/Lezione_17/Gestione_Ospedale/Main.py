from Persona import Persona
from Dottore import Dottore
from Paziente import Paziente
from Fattura import Fattura

# --- TEST PERSONA ---
print("=== TEST PERSONA ===")
p1 = Persona("Mario", "Rossi")
p1.greet()

p2 = Persona(123, "Bianchi")  # Nome non valido
p2.greet()
p2.setNome("Luca")
p2.setEta(25)
p2.greet()
print()

# --- TEST DOTTORE ---
print("=== TEST DOTTORE ===")
d1 = Dottore("Giulia", "Verdi", "Pediatra", 50.0)
d1.setEta(35)
d1.doctorGreet()
d1.isAValidDoctor()

d2 = Dottore("Anna", "Neri", "Medico Generale", "100")  # Parcella non valida
d2.setEta(40)
d2.doctorGreet()
d2.isAValidDoctor()
print()

# --- TEST PAZIENTE ---
print("=== TEST PAZIENTE ===")
pa1 = Paziente("Carlo", "Bianchi", "ID001")
pa2 = Paziente("Elena", "Russo", "ID002")
pa3 = Paziente("Marco", "Lombardi", "ID003")

pa1.InfoPaziente()
pa2.InfoPaziente()
print()

# --- TEST FATTURA ---
print("=== TEST FATTURA ===")
pazienti_list = [pa1, pa2]
fattura1 = Fattura(pazienti_list, d1)  # Dottore valido

print(f"Numero fatture: {fattura1.getFatture()}")
print(f"Salario iniziale: {fattura1.getSalario()}")

# Aggiungi un nuovo paziente
fattura1.addPaziente(pa3)
print(f"Numero fatture aggiornato: {fattura1.getFatture()}")
print(f"Salario aggiornato: {fattura1.getSalario()}")

# Rimuovi un paziente
fattura1.removePaziente("ID002")
print(f"Numero fatture dopo rimozione: {fattura1.getFatture()}")
print(f"Salario dopo rimozione: {fattura1.getSalario()}")

# Tentativo di creare fattura con dottore non valido
fattura2 = Fattura([pa1, pa2], d2)
