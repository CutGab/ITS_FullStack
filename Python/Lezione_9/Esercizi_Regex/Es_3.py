# 3. Email semplici
# Obiettivo: Definire pattern per email.

# Esercizio 3.1: Scrivi una RegEx che riconosca email del tipo nome@dominio.com.
# Esercizio 3.2: Estendi la RegEx per accettare anche domini con più estensioni, es. nome@dominio.co.uk.

import re

email: str = "gabbygab696@gmail.com"
email_2: str ="nome@dominio.co.uk"
import re

match_3_1 = re.fullmatch(r"[a-z0-9]+@[a-z]+\.com", email)
match_3_2 = re.fullmatch(r"[a-z0-9]+@[a-z]+(\.[a-z]+)+", email_2)

print(f"Email format corretto: {bool(match_3_1)}")
print(f"Email format corretto: {bool(match_3_2)}")