# La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
# Un errore nell'implementazione porta a risultati inaspettati.
# Trova l'errore e correggi il codice affinché soddisfi i casi di test.
# For example:

# Test
# print(calculate_average([1, 2, 3, 4, 5]))
# Result
# 3.0

# print(calculate_average([]))
# 0

def calculate_average(numbers: list):

    somma = 0

    if numbers == []:
        return 0

    for i in numbers:
        somma += i

    return somma/len(numbers)

print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([]))
print(calculate_average([10, 20, 30]))