# Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:

# tutti i numeri pari vengano prima di tutti i numeri dispari;

# l’ordine relativo tra pari e dispari va mantenuto;

# l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.

# For example:

# Test	Result
# print(even_odd_pattern([3, 6, 1, 8, 4, 7]))
# [6, 8, 4, 3, 1, 7]

def even_odd_pattern(numbers: list):

    even_odd_sorted: list = []
    numbers_copy: list = numbers[:]

    for i in numbers:

        if i % 2 == 0:

            even_odd_sorted.append(i)
            numbers_copy.remove(i)

    return even_odd_sorted + numbers_copy

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))
print(even_odd_pattern([3, 6, 1, 8, 4, 7, -1]))
print(even_odd_pattern([3, 6, 1, 8, 4, 7, 0, -1]))