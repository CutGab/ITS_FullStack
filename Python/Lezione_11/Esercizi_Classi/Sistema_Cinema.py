# Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

 
# Classi:
# - Film: Rappresenta un film con titolo e durata.
 
# - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
# Metodi:

#     - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
#     - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
# - Cinema: Gestisce le operazioni legate alla gestione delle sale.
# Metodi:

#     - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#     - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.
# Test case:
# Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
# Un cliente sceglie un film e prenota un certo numero di posti.
# Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

from datetime import timedelta

class Film:

    def __init__(self, titolo: str, durata: timedelta):

        self.titolo = titolo
        self.durata = durata

class Sala:

    def __init__(self, numero_ID: int, screening_film: Film, posti_totali: int, posti_prenotati: int):

        self.numero_ID = numero_ID
        self.screening_film = screening_film
        self.posti_totali = posti_totali
        self.posti_prenotati = posti_prenotati

    def posti_disponibili(self):

        return self.posti_totali - self.posti_prenotati

    def prenota_posti(self, posti_voluti):

        if posti_voluti > self.posti_disponibili():

            print("Spiacenti, posti non disponibili.")

        else:

            self.posti_prenotati += posti_voluti

class Cinema:

    def __init__(self, sale: list[Sala]):

        self.sale = sale

    def aggiungi_sala(self, sala: Sala):
         
        if any(i.numero_ID == sala.numero_ID for i in self.sale):
            
            print("Questa sala è già esistente.")
            
        else:
            self.sale.append(sala)

    def prenota_film(self, titolo_film, num_posti):
        
        for i in self.sale:

            if titolo_film == i.screening_film.titolo:

                return i.prenota_posti(num_posti)


        return "Spiacenti, film non disponibile o inesistente."


# --- Creiamo alcuni film ---
film1 = Film("Inception", timedelta(hours=2, minutes=28))
film2 = Film("Matrix", timedelta(hours=2, minutes=16))
film3 = Film("Avatar", timedelta(hours=3, minutes=12))

# --- Creiamo alcune sale ---
sala1 = Sala(numero_ID=1, screening_film=film1, posti_totali=100, posti_prenotati=10)
sala2 = Sala(numero_ID=2, screening_film=film2, posti_totali=80, posti_prenotati=5)

# --- Creiamo il cinema e aggiungiamo le sale ---
cinema = Cinema(sale=[sala1, sala2])

# Proviamo ad aggiungere una sala già esistente
sala_duplicate = Sala(numero_ID=1, screening_film=film3, posti_totali=120, posti_prenotati=0)
cinema.aggiungi_sala(sala_duplicate)  # Deve stampare "Questa sala è già esistente."

# --- Test prenotazione posti ---
print("Posti disponibili sala1 prima:", sala1.posti_disponibili())  # 90
sala1.prenota_posti(20)  # Prenotiamo 20 posti
print("Posti disponibili sala1 dopo:", sala1.posti_disponibili())   # 70

# Prenotazione tramite Cinema
cinema.prenota_film("Matrix", 10)  # Prenotiamo 10 posti per Matrix
print("Posti disponibili sala2 dopo prenotazione cinema:", sala2.posti_disponibili())  # 65

# Tentativo di prenotazione posti non disponibili
cinema.prenota_film("Matrix", 100)  # Deve stampare "Spiacenti, posti non disponibili."

# Prenotazione per film inesistente
risultato = cinema.prenota_film("Titanic", 5)
print(risultato)  # Deve stampare "Spiacenti, film non disponibile o inesistente."