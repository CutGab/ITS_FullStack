# Esercizio 6 – Uso con reduce()
# Usa reduce() (dal modulo functools) e una lambda per calcolare il prodotto di tutti gli elementi di una lista numeri = [2, 3, 4].

import functools

prodotto = lambda numeri: (functools.reduce(lambda x, y: x * y, numeri))

print(prodotto([2, 3, 4]))