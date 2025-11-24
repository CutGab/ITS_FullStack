import sys

from data_model.citta import Citta
from data_model.nazione import Nazione
from db.utils import load_nazioni

if __name__ == "__main__":

    nazioni: dict[str, Nazione] = load_nazioni()
    print(nazioni)

    sys.exit(0)