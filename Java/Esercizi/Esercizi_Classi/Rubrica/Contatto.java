// Si vuole modellare una rubrica per memorizzare contatti telefonici.
// Il contatto è definito da nome, cognome e un numero telefonico
// La rubrica dovrà fornire le seguenti funzionalità:
// Inserisci contatto
// Mostra contatto alla posizione specificata
// Stampa tutti i contatti
// Mostra il numero di contatti registrati
// Mostra il numero di posti liberi
// Cerca un contatto per nome
// Cerca un contatto per numero

// Note: la rubrica è inizialmente vuota ed avrà una dimensione fissata.



package Esercizi.Esercizi_Classi.Rubrica;

public class Contatto {

    private String nome;
    private String cognome;
    private Integer numero;

    public Contatto(String nome, String cognome, Integer numero) {
        this.nome = nome;
        this.cognome = cognome;
        this.numero = numero;
    }

    public String getNome() {
        return nome;
    }

    public String getCognome() {
        return cognome;
    }

    public Integer getNumero() {
        return numero;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setCognome(String cognome) {
        this.cognome = cognome;
    }

    public void setNumero(Integer numero) {
        this.numero = numero;
    }

    @Override
    public String toString() {
        return "Contatto [nome=" + nome + ", cognome=" + cognome + ", numero=" + numero + "]";
    }
    
}
