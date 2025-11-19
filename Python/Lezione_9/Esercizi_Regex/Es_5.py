# 5. Riconoscere date
# Obiettivo: Lavorare con formati numerici separati da caratteri speciali.

# Esercizio 5.1: Scrivi una RegEx che riconosca una data nel formato gg/mm/aaaa (es. 09/04/2025).
# Esercizio 5.2: Adatta la RegEx per accettare anche il formato gg-mm-aaaa.

import re

date_EU: str = "24/12/2003"
date_AM: str = "12-24-2003"

match_5_1 = re.fullmatch(r"\d{2}/\d{2}/\d{4}", date_EU)
match_5_2 = re.fullmatch(r"\d{2}-\d{2}-\d{4}", date_AM)

print(f"Format data europea corretto: {bool(match_5_1)}")
print(f"Format data americana corretto: {bool(match_5_2)}")