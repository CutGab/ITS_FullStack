# Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. 
# Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. 
# Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

# Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

# Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
# - se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
# - se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
# - Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Mammiferi: list = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
Rettili: list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli: list = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
Pesci: list = ["squalo", "trota", "salmone", "carpa"]
Habitats: list = ["acqua", "terra", "aria"]

animale = (input("Inserire il nome di un animale: "))
habitat = (input(f"Inserire l'habitat in cui vive l'animale {animale}: "))

match animale.lower():
    
    case animale if animale in Mammiferi:
        print(f"{animale} appartiene alla categoria dei Mammiferi!")
        animal_type = "Mammiferi"

    case animale if animale in Rettili:
        print(f"{animale} appartiene alla categoria dei Rettili!")
        animal_type = "Rettili"

    case animale if animale in Uccelli:
        print(f"{animale} appartiene alla categoria degli Uccelli!")
        animal_type = "Uccelli"

    case animale if animale in Pesci:
        print(f"{animale} appartiene alla categoria dei Pesci!")
        animal_type = "Pesci"

    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")
        animal_type = "Unknown"

match habitat:
    case habitat if habitat not in Habitats:
        print(f"Non sono in grado di fornire informazioni sull'habitat {habitat}")

animal: dict = {"Nome": animale,
                "Categoria": animal_type,
                "Habitat": habitat}

match animale.lower():

    case "balena" | "delfino" | "squalo" | "trota" | "salmone" | "carpa":
        match habitat:
            case "acqua":
                print(f"L'animale {animale} è uno dei {animal_type} che può vivere in acqua!")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")

    case "cane" | "gatto" | "cavallo" | "elefante" | "leone" | "serpente" | "lucertola":
        match habitat:
            case "terra":
                print(f"L'animale {animale} è uno dei {animal_type} che può vivere sulla terra!")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")

    case "aquila" | "pappagallo" | "gufo" | "falco":
        match habitat:
            case "aria":
                print(f"L'animale {animale} è uno dei {animal_type} che può vivere nell'aria!")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")

    case "coccodrillo" | "tartaruga":
        match habitat:
            case "terra" | "acqua":
                print(f"L'animale {animale} è uno dei {animal_type} che può vivere sia sulla terra che in acqua!")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")

    case "cigno" | "anatra":
        match habitat:
            case "aria" | "acqua":
                print(f"L'animale {animale} è uno dei {animal_type} che può vivere sia nell'aria che in acqua!")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")

    case "gallina" | "tacchino":
        match habitat:
            case "terra" | "aria":
                print(f"L'animale {animale} è uno dei {animal_type} che può vivere sulla terra e può anche volare brevemente!")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")
