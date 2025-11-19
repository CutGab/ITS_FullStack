# Sistema di Gestione Biblioteca
# Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
# Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
# Classi:
# - Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

#     Metodi della classe:
#     - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

#     - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

#     - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

#     - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

# Codice Driver
# Aggiungi libri alla biblioteca.
# Presta e restituisci libri, gestendo anche casi limite (già prestato, doppia restituzione, libro inesistente).
# Mostra i libri disponibili in ogni fase.
# Visualizza lo stato finale di ogni libro.

class Libro:

    def __init__(self, titolo: str, autore: str, stato = "Disponibile"):

        self.titolo = titolo
        self.autore = autore
        self.stato = stato

class Biblioteca:

    def __init__(self, catalogo: list[Libro]):
        
        self.catalogo = catalogo

    def aggiungi_libro(self, libro: Libro):

        if any(i.titolo == libro.titolo for i in self.catalogo):
            
            print("Questo libro è già presente nel catalogo.")
            
        else:
            self.catalogo.append(libro)

    def presta_libro(self, titolo):

        for libro in self.catalogo:

            if libro.titolo == titolo and libro.stato == "Disponibile":

                libro.stato = "Prestato"

                return f"{libro.titolo}: {libro.stato}"
            
        return "Questo libro è stato già prestato."
            
    def restituisci_libro(self, titolo):

        for libro in self.catalogo:

            if libro.titolo == titolo and libro.stato == "Prestato":

                libro.stato = "Disponibile"

                return f"{libro.titolo}: {libro.stato}"
            
        return "Questo libro è già disponibile."
    
# Creazione libri
libro1 = Libro("Il Nome della Rosa", "Umberto Eco")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien")

# Creazione biblioteca
mia_biblioteca = Biblioteca([])

# Aggiunta libri
print("Aggiunta libri:")
mia_biblioteca.aggiungi_libro(libro1)
mia_biblioteca.aggiungi_libro(libro2)
mia_biblioteca.aggiungi_libro(libro3)

# Tentativo di aggiungere un libro già presente
mia_biblioteca.aggiungi_libro(Libro("1984", "George Orwell"))

print("")

# Prestito libri
print("Prestiti:")
print(mia_biblioteca.presta_libro("1984"))      # prestito valido
print(mia_biblioteca.presta_libro("1984"))      # doppio prestito → errore
print(mia_biblioteca.presta_libro("Dracula"))   # libro inesistente

print("")

# Restituzione libri
print("Restituzioni:")
print(mia_biblioteca.restituisci_libro("1984"))   # restituzione valida
print(mia_biblioteca.restituisci_libro("1984"))   # doppia restituzione → errore
print(mia_biblioteca.restituisci_libro("Dracula")) # libro inesistente

print("")

# Mostra libri disponibili
print("Libri disponibili:")
disponibili = [libro.titolo for libro in mia_biblioteca.catalogo if libro.stato == "Disponibile"]
print(disponibili if disponibili else "Nessun libro disponibile.")

print("")

# Stato finale di tutti i libri
print("Stato finale del catalogo:")
for libro in mia_biblioteca.catalogo:
    print(f"{libro.titolo} - {libro.autore}: {libro.stato}")