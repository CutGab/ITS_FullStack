package Esercizi.Esercizi_Classi.Cartoleria;

public abstract class Articolo {

    private String marca;
    private String modello;
    private double costo;
    private double prezzo_vendita;

    public Articolo(String marca, String modello, double costo, double prezzo_vendita) {
        this.marca = marca;
        this.modello = modello;
        this.costo = costo;
        this.prezzo_vendita = this.costo * 2;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModello() {
        return modello;
    }

    public void setModello(String modello) {
        this.modello = modello;
    }

    public double getCosto() {
        return costo;
    }

    public void setCosto(double costo) {
        this.costo = costo;
    }

    public double getPrezzoVendita() {
        return prezzo_vendita;
    }

    @Override
    public String toString() {
        return "Merce [marca=" + marca + ", modello=" + modello + ", costo=" + costo + ", prezzo_vendita="
                + prezzo_vendita + "]";
    }
    
    
}
