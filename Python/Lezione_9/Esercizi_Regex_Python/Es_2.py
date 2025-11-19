# 2. Trova tutte le email in un testo
# Scrivi una funzione extract_emails(text) che prende un testo e restituisce tutte le email trovate.

# Esempio:

# text = "Contattaci a info@azienda.com oppure support@help.org"
# extract_emails(text)  # ['info@azienda.com', 'support@help.org']

import re

def extract_emails(text: str):

    match = re.findall(r"[a-z0-9]+@[a-z]+(?:\.[a-z]+)+", text)

    return match

print(extract_emails("Contattaci a info@azienda.com oppure support@help.org"))