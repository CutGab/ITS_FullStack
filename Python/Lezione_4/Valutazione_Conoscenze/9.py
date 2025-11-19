# Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
# For example:

# Test	Result
# print(remove_elements({5, 6, 7}, [7, 8, 9]))
# {5, 6}

def remove_elements(insieme: set, elementi_da_rimuovere: list):

    for i in elementi_da_rimuovere:

        if i in insieme:
            insieme.remove(i)

    return insieme


print((remove_elements({5, 6, 7}, [7, 8, 9])))
print(remove_elements({10, 20, 30}, []))