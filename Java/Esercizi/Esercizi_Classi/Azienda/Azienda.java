package Esercizi.Esercizi_Classi.Azienda;

import java.util.ArrayList;

public class Azienda {

    private String nome;
    private ArrayList <Impiegato> dipendenti;

    public Azienda(String nome) {
        this.nome = nome;
        this.dipendenti = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public ArrayList<Impiegato> getDipendenti() {
        return this.dipendenti;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        String s = "Nome azienda: " + this.nome +"\n";
        s += "Elenco dipendenti: \n";
        
        for (Impiegato impiegato : dipendenti) {
            s += impiegato.toString() + "\n";
        }
        return s;
    }

    public void assume (Impiegato impiegato) {
        this.dipendenti.add(impiegato);

    }

    public void incrementaSalarioxTutti (int Incremento) {
        for (Impiegato impiegato : dipendenti) {
            impiegato.incrementaSalario(Incremento);
            
        } 
        }
    
}
