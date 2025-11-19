# Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. 
# Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. 
# Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro 
# e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

from Pagamento import *


class PagamentoContanti(Pagamento):

    def __init__(self, importo: float):
        super().__init__()

        self.setImporto(importo)

    def dettagliPagamento(self):
        print(f"Importo del pagamento in contanti: €{self.getImporto():.2f}.")

    def inPezziDa(self):
        
        importo = self.getImporto()
        tagli = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
        
        for taglio in tagli:
            n = int(importo // taglio)

            if n > 0:
                
                if taglio in tagli[7:]:
                    print(f"{n} monete da €{taglio:.2f}")

                else:
                    print(f"{n} pezzi da €{taglio:.2f}")
            importo = importo - n * taglio
        importo = round(importo, 2)