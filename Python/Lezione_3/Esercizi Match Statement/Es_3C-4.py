# Esercizio 3C-4. Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, utilizzando un match statement, identifichi a quale categoria esso appartiene. L'animale deve essere classificato in una delle seguenti categorie:

# - Mammiferi: cane, gatto, cavallo, elefante, leone.
# - Rettili: serpente, lucertola, tartaruga, coccodrillo.
# - Uccelli: aquila, pappagallo, gufo, falco.
# - Pesci: squalo, trota, salmone, carpa.

# Se l'animale non appartiene a nessuna delle categorie sopra elencate,  mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

Mammiferi: list = ["cane", "gatto", "cavallo", "elefante", "leone"]
Rettili: list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli: list = ["aquila", "pappagallo", "gufo", "falco"]
Pesci: list = ["squalo", "trota", "salmone", "carpa"]

animale = (input("Inserire il nome di un animale: "))

match animale.lower():
    
    case animale if animale in Mammiferi:
        print(f"{animale} appartiene alla categoria dei Mammiferi!")

    case animale if animale in Rettili:
        print(f"{animale} appartiene alla categoria dei Rettili!")

    case animale if animale in Uccelli:
        print(f"{animale} appartiene alla categoria degli Uccelli!")

    case animale if animale in Pesci:
        print(f"{animale} appartiene alla categoria dei Pesci!")

    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")