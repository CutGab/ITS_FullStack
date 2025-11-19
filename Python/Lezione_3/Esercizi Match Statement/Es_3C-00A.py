# Esercizio 3C-00A. Scrivere un programma in Python che richieda all'utente di inserire un numero intero rappresentante il numero di neonati e utilizzi lo statement match per fornire una risposta appropriata:

# - Se il numero inserito è 1, stampare "Congratulazioni!"
# - Se il numero inserito è 2, stampare "Wow! Gemelli!"
# - Se il numero inserito è 3, stampare "Wow! Tre!"
# - Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
# - Se il numero inserito è 5, stampare "Incredibile! Cinque!"
# - Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito.

num = int(input("Inserisci un numero intero: "))

match num:

    case 1:
        print("Congratulazioni!")

    case 2:
        print("Wow! Gemelli!")

    case 3:
        print("Wow! Tre!")

    case 4:
        print("Mamma mia Quattro! Wow!")

    case 5:
        print("Incredibile! Cinque!")

    case n:
        print(f"Non ci credo! {n} bambini!")


