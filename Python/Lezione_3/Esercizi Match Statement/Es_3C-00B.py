# Esercizio 3C-00B. Scrivere un programma in Python che chieda all'utente di inserire il proprio nome e il proprio genere (specificato con "m" per maschio o "f" per femmina) 
# e utilizzi lo statement match per fornire una risposta adeguata da inserire in un documento di identita'.

# - Se il valore di gender è "m", stampare il nome e il genere come Maschio.
# - Se il valore di gender è "f", stampare il nome e il genere come Femmina.
# - Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore, indicando che non è possibile generare un documento di identità.

nome = input("Inserisci il tuo nome: ")
genere = input("Inserisci il tuo genere: ")

match (nome, genere):
    
    case (*_, "m"):
        print(f"Nome: {nome}\nGenere: Maschio")

    case (*_, "f"):
        print(f"Nome: {nome}\nGenere: Femmina")

    case _:
        print(f"Mi dispiace {nome}, non è possibile procedere con la generazione di un documento di identità!")

