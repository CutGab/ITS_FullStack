# Il valore di π può essere approssimato utilizzando la seguente serie infinita:

# π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

# Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate. Quindi:

# progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
# modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
# modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
# modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.

cicli = 0
numeratore = 4
denumeratore = 1
result = 0

while round(result, 2) != 3.14:
        
        if cicli % 2 != 0:
              result = result - (numeratore/ denumeratore)

        else:
               result = result + (numeratore/denumeratore)

        denumeratore += 2
        cicli += 1

print(cicli)

while round(result, 3) != 3.141:
        
        if cicli % 2 != 0:
              result = result - (numeratore/ denumeratore)

        else:
               result = result + (numeratore/denumeratore)

        denumeratore += 2
        cicli += 1

print(cicli)

while round(result, 4) != 3.1415:
        
        if cicli % 2 != 0:
              result = result - (numeratore/ denumeratore)

        else:
               result = result + (numeratore/denumeratore)

        denumeratore += 2
        cicli += 1

print(cicli)

while round(result, 5) != 3.14159:
        
        if cicli % 2 != 0:
              result = result - (numeratore/ denumeratore)

        else:
               result = result + (numeratore/denumeratore)

        denumeratore += 2
        cicli += 1

print(cicli)
