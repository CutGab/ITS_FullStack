from Persona import Persona

class Dottore(Persona):

    def __init__(self, nome, cognome, specializzazione, parcella ):
        super().__init__(nome, cognome)

        self.setSpecialization(specializzazione)
        self.setParcel(parcella)

    def setSpecialization(self, new_specializzazione):
        if isinstance(new_specializzazione, str):
            self.__specializzazione = new_specializzazione
        else:
            self.__specializzazione = None
            print("La specializzazione non è una stringa.")

    def setParcel(self, new_parcella):
        if isinstance(new_parcella, float):
            self.__parcella = new_parcella
        else:
            self.__parcella = None
            print("La parcella non è un float.")

    def getSpecialization(self):
        return self.__specializzazione
    
    def getParcel(self):
        return self.__parcella
    
    def isAValidDoctor(self):

        if self.getAge() > 30:

            print(f"Dottor {self.getName()} e {self.getLastName()} is valid!")

        else:

            print(f"Dottor {self.getName()} e {self.getLastName()} is not valid!")

    def doctorGreet(self):
        print(f"Sono un medico {self.getSpecialization()}")
        return super().greet()



d1 = Dottore ("Gabriele", "Cutolo", "chirurgo", 19.99)
d1.setAge(31)

d1.isAValidDoctor()
d1.doctorGreet()