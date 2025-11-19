from Genere import Azione, Commedia, Drama
from Noleggio import Noleggio


# Creo film di vari generi
film1 = Azione(1, "Die Hard")
film2 = Commedia(2, "Una notte da leoni")
film3 = Drama(3, "Il miglio verde")
film4 = Azione(4, "Mad Max")

# Lista di film disponibili nel negozio
catalogo = [film1, film2, film3, film4]

# Creo il negozio
Blockbuster = Noleggio(film_list=catalogo)

print("\n--- FILM DISPONIBILI ---")
Blockbuster.printMovies()

# Test disponibilità
print("\n--- TEST DISPONIBILITÀ ---")
Blockbuster.isAvailable(film2)   # disponibile
Blockbuster.isAvailable(Drama(5, "Film assente"))  # non disponibile

# Test noleggio
print("\n--- TEST NOLEGGIO ---")
Blockbuster.rentAMovie(film2, clientID=101)
Blockbuster.rentAMovie(film3, clientID=101)
Blockbuster.rentAMovie(film2, clientID=102)  # già noleggiato

print("\n--- FILM DISPONIBILI DOPO NOLEGGIO ---")
Blockbuster.printMovies()

# Test film noleggiati da cliente
print("\n--- FILM NOLEGGIATI CLIENTE 101 ---")
Blockbuster.printRentMovies(101)

# Test restituzione
print("\n--- RESTITUZIONE ---")
giorni_ritardo = 3
print(Blockbuster.giveBack(film2, clientID=101, days=giorni_ritardo))

print("\n--- FILM DISPONIBILI DOPO RESTITUZIONE ---")
Blockbuster.printMovies()

print("\n--- FILM NOLEGGIATI CLIENTE 101 DOPO RESTITUZIONE ---")
Blockbuster.printRentMovies(101)