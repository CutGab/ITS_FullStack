# Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

# Il programma deve:

# acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
# calcolare e visualizzare la somma di tutti i numeri pari inseriti;
# calcolare e visualizzare la media di tutti i numeri dispari inseriti;
# determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
# se più numeri hanno la stessa frequenza massima, visualizzarli tutti.

lista1: list = []
frequenza: dict = {}
somma_pari = 0
media_dispari = 0
j = 0

while True:

    n = int(input("Inserisci un numero (0 per terminare): "))

    if n == 0:
        break

    else:
        lista1.append(n)

        if n not in frequenza:

            frequenza[n] = 1

        else:

            frequenza[n] += 1

for i in lista1:
    if i % 2 == 0:
        somma_pari += i

    else:
        media_dispari += i
        j += 1

print(f"Somma pari: {somma_pari}\nMedia dispari: {media_dispari/j}")

max_frequenza = max(frequenza.values())

for key, values in frequenza.items():
    if values == max_frequenza:
        print(f"Numero più frequente: [{key}] ({values} volte)")