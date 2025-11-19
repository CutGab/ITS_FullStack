# 7. Verifica un nome proprio
# Scrivi una funzione is_valid_name(name) che controlla se la stringa inizia con una lettera maiuscola seguita da almeno due lettere minuscole.

# Esempio:

# is_valid_name("Marco")    # True
# is_valid_name("marco")    # False
# is_valid_name("Ma")       # False

import re

def is_valid_name(name: str):

    valid = re.fullmatch(r"[A-Z][a-z]{2,}", name)

    return bool(valid)

print(is_valid_name("Marco"))   # True
print(is_valid_name("marco"))    # False
print(is_valid_name("Ma"))       # False