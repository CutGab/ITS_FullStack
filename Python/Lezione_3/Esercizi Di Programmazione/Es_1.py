# Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
# Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.

while True:

    parola = input("Inserisci una parola: ")

    if parola.lower() == "fine":
        break

    elif parola.lower()[0] == parola.lower()[-1]:
        print("Sono uguali!")

    else:
        print("Non sono uguali.")
