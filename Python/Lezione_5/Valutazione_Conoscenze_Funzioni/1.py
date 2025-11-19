# Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
# La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.

# For example:

# Test	Result
# print(somma_elementi([1,1,1],[1,1,1]))
# [2, 2, 2]


def somma_elementi(lista1: list, lista2: list):

    lista3: list = []

    for i in range(len(lista1)):

        lista3.append(lista1[i] + lista2[i])

    return lista3

print(somma_elementi([1,2,-1],[0,-1,0]))

