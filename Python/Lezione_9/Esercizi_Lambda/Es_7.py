# Esercizio 7 – Filtra parole corte
# Hai una lista di parole parole = ["cane", "gatto", "elefante", "ratto", "orso"] Estrai solo le parole con più di 4 lettere usando filter() e lambda.

filtra = lambda parole: list(filter(lambda x: len(x) > 4, parole))

print(filtra(["cane", "gatto", "elefante", "ratto", "orso"]))