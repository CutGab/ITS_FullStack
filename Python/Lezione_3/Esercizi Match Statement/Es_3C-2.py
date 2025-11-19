# Esercizio 3C-2. Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
# Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

# - 106-110 → 4.0
# - 101-105 → 3.7
# - 96-100 → 3.3
# - 91-95 → 3.0
# - 86-90 → 2.7
# - 81-85 → 2.3
# - 76-80 → 2.0
# - 70-75 → 1.7
# - 66-69 → 1.0
# - Altro caso → "Voto non valido"

voto = int(input("Inserire un voto tra 66 e 110: "))

match voto:

    case voto if voto < 66 or voto > 110:
        print("Voto non valido.")
    
    case voto if voto == 66 or voto <= 69:
        print(1.0)

    case voto if voto == 70 or voto <= 75:
        print(1.7)

    case voto if voto == 76 or voto <= 80:
        print(2.0)

    case voto if voto == 81 or voto <= 85:
        print(2.3)

    case voto if voto == 86 or voto <= 90:
        print(2.7)

    case voto if voto == 91 or voto <= 95:
        print(3.0)

    case voto if voto == 96 or voto <= 100:
        print(3.3)

    case voto if voto == 101 or voto <= 105:
        print(3.7)

    case voto if voto == 106 or voto <= 110:
        print(4.0)