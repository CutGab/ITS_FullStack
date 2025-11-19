# Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
# Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome della forma su "Rettangolo".

# Il metodo getArea() deve calcolare l'area del rettangolo.

# Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. 

# Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

from Forma import *

class Rettangolo(Forma):

    def __init__(self, nome, base, altezza):
        super().__init__(nome)

        self.nome = "Rettangolo"
        self.base = base
        self.altezza = altezza

    def getArea(self):
        print(self.base * self.altezza)
    
    def render(self):

        print("* " * self.base)
        for _ in range(self.altezza - 2):
            print("* " + "  " * (self.base - 2) + "*")
        
        print("* " * self.base)

r1 = Rettangolo ("Rettangolo", 20, 7)

r1.render()

print("")

r1.getArea()