package Esercizi.Esercizi_Classi.Azienda;

import java.util.Date;

public class Manager extends Impiegato {

    private String segretaria;

    public Manager(String nome, double salario, Date dataAssunzione, String segretaria) {
        super(nome, salario, dataAssunzione);
        this.segretaria = segretaria;
    }
    
    //Salario parte con 2000
    public Manager(String nome, Date dataAssunzione, String segretaria) {
        super(nome, 2000 , dataAssunzione);
        this.segretaria = segretaria;
    }

    public void setSegretaria(String segretaria) {
        this.segretaria = segretaria;
    }

    public String getSegretaria() {
        return segretaria;
    }

    @Override
    public void incrementaSalario(double aumento) {
        Date oggi = new Date();
        double bonus = 0.5 * (oggi.getYear() + 1900 - this.getAnnoAssunzione());
        super.incrementaSalario(aumento + bonus);
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString() + ", segretaria = " + segretaria;
    }

    

}
