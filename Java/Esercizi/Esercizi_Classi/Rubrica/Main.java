package Esercizi.Esercizi_Classi.Rubrica;

public class Main {
    public static void main(String[] args) {
        
        // Creo la rubrica
        Rubrica rubrica = new Rubrica("Rubrica Personale");
        System.out.println("Posti disponibili iniziali: " + rubrica.showPostiDisponibli());
        
        // Creo alcuni contatti
        Contatto c1 = new Contatto("Mario", "Rossi", 12345);
        Contatto c2 = new Contatto("Luigi", "Bianchi", 67890);
        Contatto c3 = new Contatto("Anna", "Verdi", 54321);
        Contatto c4 = new Contatto("Carla", "Neri", 98765); // test limite posti
        
        // Aggiungo contatti
        rubrica.addContatto(c1);
        rubrica.addContatto(c2);
        rubrica.addContatto(c3);
        rubrica.addContatto(c4); // dovrebbe dare messaggio posti massimi
        
        // Stampo tutti i contatti
        System.out.println("\nElenco contatti:");
        System.out.println(rubrica.getAllContatti());
        
        // Cerco contatto per nome
        String nomeCercato = "Luigi";
        Contatto trovatoNome = rubrica.findContattiByNome(nomeCercato);
        System.out.println("Ricerca per nome (" + nomeCercato + "): " + (trovatoNome != null ? trovatoNome : "Non trovato"));
        
        // Cerco contatto per numero
        Integer numeroCercato = 54321;
        Contatto trovatoNumero = rubrica.findContattiByNumero(numeroCercato);
        System.out.println("Ricerca per numero (" + numeroCercato + "): " + (trovatoNumero != null ? trovatoNumero : "Non trovato"));
        
        // Mostro posti disponibili rimanenti
        System.out.println("\nPosti disponibili rimanenti: " + rubrica.showPostiDisponibli());
    }
}
