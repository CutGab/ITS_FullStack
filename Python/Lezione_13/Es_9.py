# Esercizio 9.

# Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data e restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.

# Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al fine di costruire la stringa da restituire.

vocali = ["a", "e", "i", "o", "u"]

def vowelsRemover(stringa: str):
    if stringa == "":
        return ""
    
    else:
        if stringa[0].lower() in vocali:
            return vowelsRemover(stringa[1:])
        else:
            return stringa[0] + vowelsRemover(stringa[1:])

print(vowelsRemover("calamaro"))
