# 4. CAP e codici
# Obiettivo: Lavorare con lunghezze fisse e caratteri misti.

# Esercizio 4.1: Definisci una RegEx per un CAP italiano (esattamente 5 cifre).
# Esercizio 4.2: Scrivi una RegEx che riconosca un codice fiscale italiano semplificato: 6 lettere, 2 numeri, 1 lettera, 2 numeri.

import re

cap: str = "20100"
cf: str = "ABCDEF23M45"

match_4_1 = re.fullmatch(r"[0-9]{5}", cap)
match_4_2 = re.fullmatch(r"[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}", cf)

print(f"CAP corretto {bool(match_4_1)}")
print(f"CF corretto {bool(match_4_2)}")