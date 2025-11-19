# Obiettivo:
# Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film e ne specifichi il titolo. 
# Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.
 
# Specifiche della Classe Media:
 
# Attributi:
# - title (stringa): Il titolo del media.
# - reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.
 
# Metodi:
# - set_title(self, title): Imposta il titolo del media.
# - get_title(self): Restituisce il titolo del media.
# - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
# - getMedia(self): Calcola e restituisce la media delle valutazioni.
# - getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, 
# ovvero mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
# - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
# - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
# Titolo del Film: The Shawshank Redemption
# Voto Medio: 3.80
# Giudizio: Bello
# Terribile: 10.00%
# Brutto: 10.00%
# Normale: 10.00%
# Bello: 30.00%
# Grandioso: 40.00%
# Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().

class Media:

    def __init__(self, title: str, reviews = None):
        self.set_title(title)
        self.reviews =  [] if reviews is None else reviews

    def set_title(self, new_title):
        self.title = new_title

    def get_title(self):
        return self.title

    def aggiungiValutazione(self, voto):
        if voto >= 1 and voto <= 5:
            self.reviews.append(voto)
        else:
            return "Il voto deve essere compreso tra 1 e 5."

    def getMedia(self):
        if self.reviews == []:
            return 0.0
        
        else:
            return sum(self.reviews) / len(self.reviews)

    def getRate(self):
        if self.reviews == []:
            return "Nessuna recensione"
        
        media = round(self.getMedia())

        if media == 1:
            return "Terribile"
        
        if media == 2:
            return "Brutto"
        
        if media == 3:
            return "Normale"
        
        if media == 4:
            return "Bello"
        
        if media == 5:
            return "Grandioso"
        
    def ratePercentage(self, voto):
        if self.reviews == []:
            return 0.0
        
        else:
            return (self.reviews.count(voto) / len(self.reviews)) * 100
        
    def recensione(self):

        return f"Nome Film: {self.get_title()}\nVoto Medio: {self.getMedia()}\nGiudizio: {self.getRate()}\nTerribile: {self.ratePercentage(1):.2f}%\nBrutto: {self.ratePercentage(2):.2f}%\nNormale: {self.ratePercentage(3):.2f}%\nBello: {self.ratePercentage(4):.2f}%\nGrandioso: {self.ratePercentage(5):.2f}%"


class Film(Media):

    def __init__(self, titolo, reviews=None):
        super().__init__(titolo, reviews)

film1 = Film("The Shawshank Redemption")
film2 = Film("Inception")

for voto in [5,4,5,4,3,5,4,5,3,4]:
    film1.aggiungiValutazione(voto)

for voto in [3,2,4,5,4,3,2,5,4,3]:
    film2.aggiungiValutazione(voto)

print(film1.recensione())
print()
print(film2.recensione())
