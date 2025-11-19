# Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del triangolo 
# (per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).

# Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".

# Il metodo getArea() deve calcolare l'area del triangolo.

# Il metodo render() deve stampare su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel costruttore. 
# Il triangolo da stampare deve essere un triangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
 
# Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare come termina ogni chiamata a print,
#  e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa riga, separate da uno spazio.

from Forma import *

class Triangolo(Forma):

    def __init__(self, nome, lato):
        super().__init__(nome)

        self.nome = "Triangolo"
        self.lato = lato

    def getArea(self):
        print((self.lato ** 2) / 2)
            
    def render(self):
        for i in range(self.lato):
            for j in range(self.lato):
                if i == self.lato - 1 or j == 0 or i == j:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()


t1 = Triangolo ("Triangolo", 8)

t1.render()

print("")

t1.getArea()