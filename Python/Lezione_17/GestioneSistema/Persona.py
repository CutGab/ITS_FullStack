class Persona:

    def __init__(self, nome: str, cognome: str):

        self.setName(nome)
        self.setLastName(cognome)
        self.__eta = 0 if isinstance(nome, str) and isinstance(cognome, str) else None

    def setName(self, new_nome):
        if isinstance(new_nome, str):
            self.__nome = new_nome
        else:
            self.__nome = None
            print("Il nome non è una stringa.")

    def setLastName(self, new_cognome):
        if isinstance(new_cognome, str):
            self.__cognome = new_cognome
        else:
            self.__cognome = None
            print("Il cognome non è una stringa.")

    def setAge(self, new_eta):
        self.__eta = new_eta if isinstance(new_eta, int) else print("L'età deve essere un numero intero.")

    def getName(self):
        return self.__nome
    
    def getLastName(self):
        return self.__cognome
    
    def getAge(self):
        return self.__eta

    def greet(self):

        if isinstance(self.getName(), str) and isinstance(self.getLastName(), str):
            print(f"Ciao sono {self.getName()} {self.getLastName()}, ho {self.getAge()} anni!")

    