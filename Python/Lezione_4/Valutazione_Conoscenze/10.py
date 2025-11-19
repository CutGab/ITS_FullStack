# Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

# For example:

# Test	Result
# print(merge_dictionaries({'x': 5}, {'x': -5}))
# {'x': 0}


def merge_dictionaries(dict1: dict, dict2: dict):

    for key, values in dict2.items():

        if key in dict1:

            dict1[key] = dict1[key] + values

        else:
            dict1[key] = values

    return dict1

print(merge_dictionaries({'x': 5}, {'x': -5}))
print(merge_dictionaries({}, {'a': 10, 'b': 20}))
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))