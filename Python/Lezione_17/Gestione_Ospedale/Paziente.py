# ### CLASSE: Paziente
# Creare un file chiamato "paziente.py".
# In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

# Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
# - Definire i seguenti metodi:
# costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
# setIdCode(idCode): consente di impostare il codice identificativo del paziente.
# getidCode(): consente di ritornare il codice identificativo del paziente.
# patientInfo(): stampa in output le informazioni del paziente in questo modo:
#         "Paziente: {nome} {cognome}
#          ID: {codice identificativo}"
 

from Persona import *

class Paziente(Persona):

    def __init__(self, nome, cognome, ID):
        super().__init__(nome, cognome)
        
        self.setCodiceID(ID)

    def setCodiceID(self, new_ID):

        if isinstance(new_ID, str):
            self.__ID = new_ID

        else:
            print("ID non valido!")
            self.__ID = None

    def getCodiceID(self):
        return self.__ID
    
    def InfoPaziente(self):

        print(f"Paziente: {self.getNome()} {self.getCognome()}\nID: {self.getCodiceID()}")

