# Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
# Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
# Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

# NOTA.
# Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
# Usare il match statement.

cont_t = 0
cont_c = 0

for i in range(8):
    lancio = input("Inserisci Testa o Croce (T/C): ")

    match lancio:

        case "t" | "T":
            cont_t += 1

        case "c" | "C":
            cont_c += 1

print(f"Totale Testa: {cont_t}\Percentuale testa: {(cont_t/8) * 100:.2f}%")
print(f"Totale Croce: {cont_t}\Percentuale croce: {(cont_c/8) * 100:.2f}%")