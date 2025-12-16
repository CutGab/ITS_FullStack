package Esercizi.Esercizi_Classi.Cartoleria;

public class Penna extends Merce {

    private String colore;

    public Penna(String marca, String modello, double costo, double prezzo_vendita, String colore) {
        super(marca, modello, costo, prezzo_vendita);
        this.colore = colore;
    }

    public String getColore() {
        return colore;
    }
    
}