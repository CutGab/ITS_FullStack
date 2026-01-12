package Esercizi.Esercizi_Classi.Cartoleria;

public abstract class Cliente {

    private String anagrafica;

    public Cliente(String anagrafica) {
        super();
        this.anagrafica = anagrafica;
    }

    public String getAnagrafica() {
        return anagrafica;
    }

    public void setAnagrafica(String anagrafica) {
        this.anagrafica = anagrafica;
    }
    @Override
    public String toString() {
        return "anagrafica=" + anagrafica;
    }

    public abstract void paga(double importo);

}

    