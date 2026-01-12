package Esercizi.Esercizi_Classi.Cartoleria;

public class Azienda extends Cliente{
    
    private double saldoCc;

    public Azienda(String anagrafica, double saldo) {
        super(anagrafica);
        this.saldoCc = saldo;
    }

    public double getSaldo() {
        return saldoCc;
    }

    public void setSaldo(double saldo) {
        this.saldoCc = saldo;
    }

    @Override
    public void paga(double importo) {
        if (saldoCc > importo) {
            saldoCc = (saldoCc - (importo / 10));
        }        
    }

    @Override
    public String toString() {
        return "Azienda: " + super.toString() + ", saldoCc=" + saldoCc;
    }

    
}


