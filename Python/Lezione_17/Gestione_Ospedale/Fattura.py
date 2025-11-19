# ### CLASSE: Fattura
# Creare un file chiamato "fatture.py".
# In tale file, creare una classe chiamata Fattura.

# - Definire i seguenti metodi:
# init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). 
# In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int).  
# In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".

# getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.

# getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.

# addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary(). 
# Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"

# removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, 
# aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). 
# Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".

from Paziente import *
from Dottore import *

class Fattura:

    def __init__(self, pazienti: list, dottore: Dottore):

        if dottore.isAValidDoctor() == True:

            self.dottore = dottore
            self.pazienti = pazienti
            self.getFatture()
            self.salario = 0

        else:
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

            self.dottore = None
            self.pazienti = None
            self.fatture = None
            self.salario = None

    def getSalario(self):

        self.salario = self.dottore.getParcella() * len(self.pazienti)
        return self.salario
    
    def getFatture(self):

        self.fatture = len(self.pazienti)
        return self.fatture
    
    def addPaziente(self, new_paziente: Paziente):

        paziente_esiste = False
        for paziente in self.pazienti:
            if paziente.getCodiceID() == new_paziente.getCodiceID():
                paziente_esiste = True
                break

        if not paziente_esiste:
            self.pazienti.append(new_paziente)
            self.getFatture()
            self.getSalario()
            print(f"Alla lista del Dottor {self.dottore.getCognome()} è stato aggiunto il paziente {new_paziente.getCodiceID()}")


    def removePaziente(self, ID):

        paziente_trovato = False
        for paziente in self.pazienti:
            if paziente.getCodiceID() == ID:
                self.pazienti.remove(paziente)
                paziente_trovato = True
                break 
        
        if paziente_trovato:
            self.getFatture()
            self.getSalario()
            print(f"Alla lista del Dottor {self.dottore.getCognome()} è stato rimosso il paziente {ID}")
        else:
            print(f"Nessun paziente con ID {ID} trovato nella lista")
