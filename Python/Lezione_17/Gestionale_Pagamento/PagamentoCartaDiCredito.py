# Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
# Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. 
# Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

from Pagamento import *
from datetime import date
import re

class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, importo: float, titolare_carta: str, data_scadenza: date, n_carta: str):
        super().__init__()
        
        self.setImporto(importo)
        self.titolare_carta = titolare_carta
        self.data_scadenza = data_scadenza if r'^(0[1-9]|1[0-2])\/(\d{2}|\d{4})$' else None
        self.n_carta = n_carta if r'^\d{16}$' else None

    def dettagliPagamento(self):
        print(f"Titolare Carta: {self.titolare_carta}\nData Scadenza Carta: {self.data_scadenza}\nNumero Carta: {self.n_carta}")
        return super().dettagliPagamento()
    

    