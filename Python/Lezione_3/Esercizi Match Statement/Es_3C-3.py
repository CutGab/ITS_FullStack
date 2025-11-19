 
# Esercizio 3C-3. Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
# Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

# - ["penna", "matita", "quaderno"] → "Materiale scolastico"
# - ["pane", "latte", "uova"] → "Prodotti alimentari"
# - ["sedia", "tavolo", "armadio"] → "Mobili"
# - ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
# - Qualsiasi altra lista → "Categoria sconosciuta"

Oggetti: list = []

for i in range(3):
    oggetto = (input("Inserire un oggetto: "))
    Oggetti.append(oggetto.lower())


match Oggetti:

    case Oggetti if Oggetti == ['penna', 'matita', 'quaderno']:
        print("Materiale scolastico")

    case Oggetti if Oggetti == ['pane', 'latte', 'uova']:
        print("Prodotti Alimentari")

    case Oggetti if Oggetti == ['sedia', 'tavolo', 'armadio']:
        print("Mobili")

    case Oggetti if Oggetti == ['telefono', 'computer', 'tablet']:
        print("Dispositivi Elettronici")

    case _:
        print("Categoria Sconosciuta")