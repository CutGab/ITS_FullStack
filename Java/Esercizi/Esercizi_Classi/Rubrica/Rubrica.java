package Esercizi.Esercizi_Classi.Rubrica;

import java.util.ArrayList;

public class Rubrica {

    private String nome;
    private ArrayList<Contatto> contatti;
    private Integer posti_disponibili;

    public Rubrica(String nome) {
        this.nome = nome;
        this.posti_disponibili = 3;
        this.contatti = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public ArrayList<Contatto> getContatti() {
        return contatti;
    }

    public void addContatto (Contatto contatto) {
        if (this.posti_disponibili > 0) {
            this.contatti.add(contatto);
            posti_disponibili--;
        } else {
            System.out.println("Posti massimi raggiunti.");
        }
    }

    public Contatto findContatto (Integer position) {
        return this.contatti.get(position);
    }

    public String getAllContatti() {
        for (Contatto contatto : contatti) 
            return contatto.toString();
        return null;
    }
    
    public Integer getTotContatti() {
        Integer i = 0;
        for (Contatto contatto : contatti) 
            i++;
        return i;
    }

    public Integer showPostiDisponibli () {
        return posti_disponibili;
    }

    public Contatto findContattiByNome (String nome) {

        for (Contatto contatto : contatti) {
            if (contatto.getNome().toLowerCase().equals(nome.toLowerCase())) {
                return contatto;
            }
        }
        return null;
    }


    public Contatto findContattiByNumero (Integer numero) {

        for (Contatto contatto : contatti) {
            if (contatto.getNumero() != null && contatto.getNumero().equals(numero)) {
                return contatto;
            }
        }
        return null;
    }


}
