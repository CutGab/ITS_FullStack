# 2. Riconoscere parole
# Obiettivo: Lavorare con lettere e lunghezze di stringhe.

# Esercizio 2.1: Scrivi una RegEx che riconosca una parola composta solo da lettere minuscole.
# Esercizio 2.2: Adatta la RegEx per accettare parole con lettere maiuscole e minuscole.
# Esercizio 2.3: Modifica la RegEx per accettare parole lunghe da 5 a 10 caratteri.

import re

text: str = "aAaAaAaAaA"

match_2_1 = re.fullmatch(r"[a-z]+", text)

print(f"Solo minuscole: {bool(match_2_1)} ")

match_2_2 = re.fullmatch(r"[A-Za-z]+", text)

print(f"Sia maiuscole che minuscole: {bool(match_2_2)}")

match_2_3 = re.fullmatch(r"[A-Za-z]{5,10}", text)

print(f"Sia maiuscole che minuscole solo se lunghe da 5 a 10 caratteri: {bool(match_2_3)}")