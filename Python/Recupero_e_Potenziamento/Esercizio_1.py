# Dato un vettore v, rappresentato da una lista di numeri interi di lunghezza n, 
# si definisce baricentro del vettore v l'indice "i" per cui si ha che la somma di tutti gli elementi della lista 
# fino all'elemento in posizione i è uguale alla somma di tutti gli elementi della lista dall'elemento in posizione i+1 fino all'ultimo elemento, ovvero:

# v[0] + v[1] + v[2] + v[3] + ... + v[i] = v[i+1] + v[i+2] + [vi+3] + ... + v[n-1]

# Ad esempio, se v = [1, 2, 3, 3, 2, 1] per tale vettore v esiste il baricentro e tale baricentro è dato dall'indice i=2. Infatti, se i=2, si ha che:


# v[0] + v[1] + v[2] = v[3] + v[4] + v[5]

# ovvero

# 1 + 2 + 3 = 3 + 2 + 1 -> 6 = 6

# Implementare quanto segue:
 

# 1.A scrivere una funzione Python chiamata baricentro(v: list[int]) che data in input una lista di numeri interi determina se per tale lista esiste il baricentro, 
# ovvero esiste un indice i per cui vale la formula scritta sopra. Se esiste ritornare l'indice, se non esiste ritornare None.

# 1.B Scrivere una funzione printResult(v: list[int]) che data in input una lista di numeri interi stampi a schermo se esiste o meno il baricentro della lista v. 
# Nel caso in affermativo, si mostri in output l'indice che definisce il baricentro.

def baricentro(v: list[int]) -> bool:

    for i in range(len(v)):
        if sum(v[:i+ 1]) == sum(v[i+ 1:]):
            return i
    
    else:
        return None




def printResult(v: list[int]) -> bool:
    
    if baricentro(v):
        print(f"Esiste il baricentro del vettore {v} ed è dato dall'indice {baricentro(v)}!")
        
    else:
        print(f"Il baricentro del vettore {v} non esiste!")

#TEST 1
baricentro([1, 2, 3, 2, 5, 2, 1])
printResult([1, 2, 3, 2, 5, 2, 1])

#TEST 2
baricentro([2, 0, -1, 4, 6, 3, -1])
printResult([2, 0, -1, 4, 6, 3, -1])

# 1.C Scrivere una funzione Python baricentroOttimizzato(v: list[int]) che determina se esiste il baricentro della lista v. 
# In questo caso, il codice dovrà fare al più due accessi ad ogni elemento della lista v.
# Suggerimento. Utilizzare due cicli separati:
 

# Nel primo ciclo, calcolare la somma totale degli elementi della lista.
# Nel secondo ciclo, accumulare progressivamente la somma degli elementi a sinistra di ciascun indice e, usando la somma totale, 
# calcolare quella a destra senza ulteriori accessi diretti agli elementi.

def baricentroOttimizzato(v: list[int]):
    total = sum(v)
    left_sum = 0

    for i, val in enumerate(v):
        right_sum = total - left_sum - val
        if left_sum + val == right_sum:
            return i
        
        else:
            left_sum += val

    return (f"Il baricentro del vettore {v} non esiste!")

print(baricentroOttimizzato([1, 2, 3, 2, 5, 2, 1]))
print(baricentroOttimizzato([2, 0, -1, 4, 6, 3, -1]))