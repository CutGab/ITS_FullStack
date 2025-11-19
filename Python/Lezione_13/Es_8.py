# Esercizio 8.

# Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

# Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
# L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.

vocali = ["a", "e", "i", "o", "u"]

def vowelsCounter(stringa: str):

    if stringa == "":
        return 0
    
    else:

        if stringa[0].lower() in vocali:
            
            return vowelsCounter(stringa[1:]) + 1
        else:
            return vowelsCounter(stringa[1:])

print(vowelsCounter("CIaOO"))