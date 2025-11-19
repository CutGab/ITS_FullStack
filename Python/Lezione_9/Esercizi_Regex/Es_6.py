# 6. Codici personalizzati
# Obiettivo: Unire lettere, numeri e caratteri speciali.

# Esercizio 6.1: Scrivi una RegEx per identificare un codice prodotto nel formato PROD-1234-XY.
# Esercizio 6.2: Crea una RegEx per un ID alfanumerico di esattamente 8 caratteri, che può contenere lettere maiuscole e numeri (es. AB12CD34).

import re

prodotto: str = "PROD-1234-XY"
id: str = "AB12CD34"

match_6_1 = re.fullmatch(r"PROD-[0-9]{4}-[A-Z]{2}", prodotto)
match_6_2 = re.fullmatch(r"[A-Z0-9]{8}", id)

print(f"Format prodotto corretto: {bool(match_6_1)}")
print(f"Format ID corretto: {bool(match_6_2)}")

