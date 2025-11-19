# Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

# Scrivere un programma che:

# Acquisisca in input un valore N (numero di euro disponibili).
# Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
# Mostri quanti buoni sconto avanzano al termine dell'acquisto.

soldi = int(input("Inserisci il numero di soldi disponibili: "))
buoni_sconto = 0
barrette = 0

for i in range(soldi):

    buoni_sconto += 1
    barrette += 1

    if buoni_sconto == 6:
        barrette += 1
        buoni_sconto = 0

print(f"Puoi comprare {barrette} barrette.\nTi rimangono {buoni_sconto} buoni sconto.")