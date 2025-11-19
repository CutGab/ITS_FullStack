# Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
# Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
# Il metodo getArea() deve calcolare l'area del quadrato.
# Il metodo render() deve stampare su schermo un quadrato avente lato pari al valore passato nel costruttore. 
# Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

from Forma import *

class Quadrato(Forma):

    def __init__(self, nome, lato):
        super().__init__(nome)

        self.nome = "Quadrato"
        self.lato = lato

    def getArea(self):
        print(self.lato * self.lato)
    
    def render(self):

        print("* " * self.lato)
        for _ in range(self.lato - 2):
            print("* " + "  " * (self.lato - 2) + "*")
        
        print("* " * self.lato)

q1 = Quadrato ("Quadrato", 5)

q1.render()

print("")

q1.getArea()