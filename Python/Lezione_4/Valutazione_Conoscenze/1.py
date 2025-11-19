# Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
# For example:

# Test
# print(list_statistics([1, 2, 3, 4, 5]))

# Result
# (5, 1, 3.0)

def list_statistics(numbers: list):

    max_num = max(numbers)
    min_num = min(numbers)
    somma = 0

    for i in numbers:

        somma += i

    return max_num, min_num, somma/len(numbers)


print(list_statistics([1, 2, 3, 4, 5]))

