package Esercizi.Esercizi_Classi.Cartoleria;

public class Gomma extends Merce {

    private double dimensione;
    private String forma;

    
    public Gomma(String marca, String modello, double dimensione, String forma, double costo, double prezzo_vendita) {
        super(marca, modello, costo, prezzo_vendita);
        this.dimensione = dimensione;
        this.forma = forma;
    }


    public double getDimensione() {
        return dimensione;
    }


    public void setDimensione(double dimensione) {
        this.dimensione = dimensione;
    }


    public String getForma() {
        return forma;
    }
    
}
