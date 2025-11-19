# Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

lista1: list = [1,2,3,4,5,6,7,8,9,10]
lista2: list = [15,13,12,17,21,34,11,2,18,23]
lista3: list = []

for i in range(len(lista1)):

    somma = lista1[i] + lista2[-i - 1]
    lista3.append(somma)

print(f"Prima Lista: {lista1}\nSeconda Lista: {lista2}\nTerza Lista Somma Incrociata: {lista3}")

