# 1. Riconoscere numeri
# Obiettivo: Definire una RegEx che riconosca solo stringhe composte da cifre.

# Esercizio 1.1: Scrivi una RegEx che riconosca un numero intero positivo (es. 123, 98765).
# Esercizio 1.2: Modifica la RegEx per accettare anche numeri negativi (es. -45, -1000, 0).

import re

text: str = "-9"

match = re.fullmatch(r"\d+", text)
match_2 = re.fullmatch(r"-?\d+", text)

print(f"Positivo: {bool(match)}")
print(f"Sia Positivo che Negativo: {bool(match_2)}")
