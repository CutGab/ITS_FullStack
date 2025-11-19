# 6. Verifica un codice prodotto
# Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.

# Esempio:

# check_product_code("PROD-9876-ZX")  # True
# check_product_code("PROD-99-ZX")    # False

import re

def check_product_code(code: str):

    match = re.fullmatch(r"PROD-[0-9]{4}-[A-Z]{2}", code)

    return bool(match)

print(check_product_code("PROD-9876-ZX"))  # True
print(check_product_code("PROD-99-ZX"))   # False