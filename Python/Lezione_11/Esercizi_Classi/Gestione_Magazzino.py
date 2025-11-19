# Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

# Definisci una classe Prodotto con i seguenti attributi:
# - nome (stringa)
# - quantità (intero)
 
# Definisci una classe Magazzino con i seguenti metodi:
# - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
# - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
# - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
# Test case:
# Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
# Il sistema cerca un prodotto per verificare se esiste nell'inventario.
# Il sistema verifica la disponibilità dei prodotti in inventario.

class Prodotto:

    def __init__(self, nome: str, quantita: int):

        self.nome = nome
        self.quantita = quantita

class Magazzino:

    def __init__(self, magazzino: list[Prodotto] = []):

        self.magazzino = magazzino

    def aggiungi_prodotto(self, prodotto: Prodotto):

        self.magazzino.append(prodotto)

    def cerca_prodotto(self, nome):

        for prodotto in self.magazzino:

            if nome == prodotto.nome:

                return prodotto.nome, prodotto.quantita
            
        return "Spiacenti, prodotto non trovato."
    
    def verifica_disponibilita(self, nome):

        for prodotto in self.magazzino:

            if prodotto.nome == nome:

                if prodotto.quantita > 0:

                    return f"Quantità del prodotto {prodotto.nome}: {prodotto.quantita}"
                
                return f"Prodotto {prodotto.nome} non disponibile."
        
        return "Prodotto non trovato."
    
# Creazione del magazzino
magazzino = Magazzino()

# Creazione dei prodotti
p1 = Prodotto("Pane", 10)
p2 = Prodotto("Latte", 0)
p3 = Prodotto("Uova", 30)

# Aggiunta dei prodotti al magazzino
magazzino.aggiungi_prodotto(p1)
magazzino.aggiungi_prodotto(p2)
magazzino.aggiungi_prodotto(p3)

# Ricerca di un prodotto
print(magazzino.cerca_prodotto("Latte"))  # Ritorna oggetto Prodotto

# Verifica disponibilità
print(magazzino.verifica_disponibilita("Latte"))  # Prodotto non disponibile
print(magazzino.verifica_disponibilita("Pane"))   # Quantità disponibile
print(magazzino.verifica_disponibilita("Acqua"))  # Prodotto non trovato