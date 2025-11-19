# Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.
# Test
# print(rounded_average([1, 1, 2, 2]))
# Result
# 2

def rounded_average(numbers:  list):

    media = sum(numbers)/len(numbers)

    return round(media)


print(rounded_average([1, 1, 2, 2]))
print(rounded_average([1, 2, 3, 4, 5]))
print(rounded_average([1, 1, 2, 2]))
print(rounded_average([10, 20, 30]))
print(rounded_average([15, 15, 14, 16]))
print(rounded_average([100, 200, 300, 400]))