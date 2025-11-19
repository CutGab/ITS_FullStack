# ### CLASSE: Persona
# Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome, ed un attributo privato di tipo int per l'età.

# - La classe Persona deve avere i seguenti metodi:

# init(first_name, last_name). 
# Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo, impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio, "Il nome inserito non è una stringa!". 
# Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; se first_name e last_name non sono due stringhe, allora assegnare None all'età.

# setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. 
# In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".

# setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. 
# Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".

# setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. 
# Il valore viene modificato se e solo se viene passato al metodo un numero intero. In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".

# getName(): consente di ritornare il nome di una persona.

# getLastname(): consente di ritornare il cognome di una persona.

# getAge(): consente di ritornare l'età di una persona.

# greet(): stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"


class Persona:

    def __init__(self, nome, cognome):

        self.setNome(nome)
        self.setCognome(cognome)
        self.__eta = 0 if self.__nome is not None and self.__cognome is not None else None

    def setNome(self, new_nome):

        if isinstance(new_nome, str):
            self.__nome = new_nome

        else:
            print("Il nome inserito non è una stringa!")
            self.__nome = None

    def setCognome(self, new_cognome):

        if isinstance(new_cognome, str):
            self.__cognome = new_cognome

        else:
            print("Il cognome inserito non è una stringa!")
            self.__cognome = None

    def setEta(self, new_eta):

        if isinstance(new_eta, int):
            self.__eta = new_eta

        else:
            print("L'età deve essere un numero intero!")


    def getNome(self):
        return self.__nome
    
    def getCognome(self):
        return self.__cognome
    
    def getEta(self):
        return self.__eta
    
    def greet(self):

        if isinstance (self.__nome, str) and isinstance(self.__cognome, str):
            print(f"Ciao, sono {self.getNome()} {self.getCognome()}! Ho {self.getEta()} anni!")