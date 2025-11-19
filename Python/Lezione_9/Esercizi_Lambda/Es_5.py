# Esercizio 5 – Funzione lambda con if
# Crea una funzione lambda che prenda un numero e ritorni "pari" se è divisibile per 2, altrimenti "dispari".

pari_dispari = lambda x: "Pari" if x % 2 == 0 else "Dispari"

print(pari_dispari(5))
print(pari_dispari(10))