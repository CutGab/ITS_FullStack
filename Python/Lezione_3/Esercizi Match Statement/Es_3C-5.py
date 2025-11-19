# Esercizio 3C-5. Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. 
# Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. 
# Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

# - Admin → "Accesso completo a tutte le funzionalità."
# - Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
# - Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
# - Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
# - Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
# - Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"

utente: dict = {}

nome = (input("Inserire il nome dell'utente: "))
utente["Nome"] = nome

ruolo = (input("Inserire il ruolo dell'utente: "))
utente["Ruolo"] = ruolo

eta = (int(input("Inserire l'età dell'utente: ")))
utente["Età"] = eta

match ruolo:

    case ruolo if ruolo == "Admin":
        print("Accesso completo a tutte le funzionalità.")

    case ruolo if ruolo == "Moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni.")
    
    case ruolo if ruolo == "Ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")

    case ruolo if ruolo == "Utente" and eta >= 18:
        print("Accesso standard a tutti i servizi.")

    case ruolo if ruolo == "Utente" and eta < 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate.")

    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")



