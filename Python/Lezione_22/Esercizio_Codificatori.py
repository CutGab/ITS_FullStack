from string import ascii_lowercase
from abc import ABC

class CodificatoreMessaggio(ABC):

    def codifica(TestoInChiaro: str):
        pass
    
class DecodificatoreMessaggio(ABC):
    
    def decodifica(TestoCodificato: str):
        pass

class Cifratore_A_Scorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int):
        self.chiave = chiave

    def codifica(self, TestoInChiaro):
        TestoCodificato = ""

        for i in TestoInChiaro.lower():
            if i in ascii_lowercase:
                pos = (ascii_lowercase.index(i) + self.chiave) % 26
                TestoCodificato += ascii_lowercase[pos]

        return TestoCodificato

    def decodifica(self, TestoCodificato):
        TestoInChiaro = ""

        for i in TestoCodificato.lower():
            if i in ascii_lowercase:
                pos = (ascii_lowercase.index(i) - self.chiave) % 26
                TestoInChiaro += ascii_lowercase[pos]

        return TestoInChiaro


# Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato n. 
# Si definisca il metodo codifica(testoInChiaro) così che il messaggio sia combinato n volte. 
# Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna delle metà in modo alternato. 
# Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi' (nel caso in cui la lunghezza del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà). 
# Il messaggio combinato è 'afbgchdie'.

# Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

class Cifratore_A_Combinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    
    def __init__(self, n: int):
        self.n = n

    def dividi(self, testo: str) -> str:
        metà = (len(testo) + 1) // 2
        prima_metà = testo[:metà]
        seconda_metà = testo[metà:]

        return prima_metà, seconda_metà

    def codifica(self, TestoInChiaro):
        TestoCodificato = TestoInChiaro
        
        for _ in range(self.n):
            # parti = self.dividi(TestoCodificato)
            # prima = parti[0]
            # seconda = parti[1]

            prima, seconda = self.dividi(TestoCodificato)

            nuovo_testo = ""

            for i in range(len(seconda)):
                nuovo_testo += prima[i] + seconda[i]

            if len(prima) > len(seconda):
                nuovo_testo += prima[-1]

            TestoCodificato = nuovo_testo

        return TestoCodificato
    
    def decodifica(self, TestoCodificato):
        TestoInChiaro = TestoCodificato
        
        for _ in range(self.n):
            parti = self.dividi(TestoInChiaro)
            prima = parti[0]
            seconda = parti[1]

            nuovo_testo = ""

            for i in range(len(seconda)):
                nuovo_testo += prima[i] + seconda[i]

            if len(prima) > len(seconda):
                nuovo_testo += prima[-1]

            TestoInChiaro = nuovo_testo

        return TestoInChiaro




c2: Cifratore_A_Combinazione = Cifratore_A_Combinazione (3)

print(c2.codifica("Ciaoo"))
print(c2.decodifica("Caoio"))


c: Cifratore_A_Scorrimento = Cifratore_A_Scorrimento (3)

print(c.codifica("zebra"))     #cheud
print(c.decodifica("cheud"))   #zebra
