# Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). 
# L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

# Il programma deve:

# Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
# Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).

numeri: list = []
numeri_interi: list = []
i = 0
j = 0

while True:

    num = float(input("Inserisci un numero: "))

    if num < 0:
        break

    elif num.is_integer() == True:
        numeri_interi.append(num)
        numeri.append(num)
        i += 1

    else:
        numeri.append(num)
        j += 1


print(numeri)
print(numeri_interi)
print(f"Numero più grande: {max(numeri)}\nNumero più piccolo: {min(numeri)}\nMedia: {sum(numeri_interi)/i}")

