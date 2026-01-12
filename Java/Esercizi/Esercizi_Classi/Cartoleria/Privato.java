package Esercizi.Esercizi_Classi.Cartoleria;

public class Privato extends Cliente {

    private double cash;

    public Privato(String anagrafica, double cash) {
        super(anagrafica);
        this.cash = cash;
    }

    public double getCash() {
        return cash;
    }

    public void setCash(double cash) {
        this.cash = cash;
    }

    @Override
    public void paga(double importo) {
        if (cash > importo) {
            cash = cash - importo;
        }        
    }

    @Override
    public String toString() {
        return "Privato: " + super.toString() + ", cash=" + cash;
    }

    
}
