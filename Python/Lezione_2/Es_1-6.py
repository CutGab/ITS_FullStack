# 1-6. Inserire all'interno di un dizionario il menu' di un ristorante, che viene specificato alla fine della traccia di questo esercizio.

# Aggiungere in un nuovo dizionario chiamato ordine, un primo, un secondo, un contorno, una bevanda ed un dolce preso dal menu'. 

# Stampare a schermo il conto totale che il cliente dovrà pagare. 

# ITS Bakery Menu':

# Pizza: 9.00 euro

# Pasta: 10.50 euro

# Zuppa : 7.00 euro

# Hamburger: 15.50 euro

# Cotoletta: 10.00 euro

# Salmone: 20.20 euro

# Patatine Fritte: 5.50 euro

# Patate al forno: 5.50 euro

ITS_menu: dict = {"Pizza": 9.00,
                "Pasta": 10.50,
                "Zuppa": 7.00,
                "Hamburger": 15.50,
                "Cotoletta": 10.00,
                "Salmone": 20.20,
                "Patatine Fritte": 5.50,
                "Patate dolci al forno": 5.50
                }

ITS_ordine: dict = {"Primo": "Pizza",
                    "Secondo": "Cotoletta",
                    "Dolce": "Patate dolci al forno"
}

Totale = 0

for piatto in ITS_ordine.values():
    if piatto in ITS_menu:
        Totale = Totale + ITS_menu[piatto]

print(Totale)