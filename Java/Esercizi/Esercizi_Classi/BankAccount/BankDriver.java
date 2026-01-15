package Esercizi.Esercizi_Classi.BankAccount;

public class BankDriver {

    public static void main(String[] args) {

        // --- TEST Conto Corrente Standard ---
        System.out.println("=== Conto Corrente Standard ===");
        ContiCorrenti conto1 = new ContiCorrenti("Mario Rossi", 12345, 500.0);

        // Versamento
        conto1.doMovimento(new Movimento(TipoMovimento.versamento, 200.0));
        // Prelievo
        conto1.doMovimento(new Movimento(TipoMovimento.prelievo, 100.0));

        // Controllo saldo
        conto1.CheckBalance();

        // Stampa dettagli conto
        System.out.println(conto1.showContoDetails());

        System.out.println("");

        // --- TEST Conto Risparmio (Savings) ---
        System.out.println("\n=== Conto Risparmio ===");
        Savings contoRisparmio = new Savings("Luigi Bianchi", 54321, 1000.0, 2.5, 3);

        // Versamento
        contoRisparmio.doMovimento(new Movimento(TipoMovimento.versamento, 500.0));

        // Prelievi
        try {
            contoRisparmio.doMovimento(new Movimento(TipoMovimento.prelievo, 200.0));
            contoRisparmio.doMovimento(new Movimento(TipoMovimento.prelievo, 100.0));
            contoRisparmio.doMovimento(new Movimento(TipoMovimento.prelievo, 50.0));
            // Questo prelievo dovrebbe generare eccezione perché max prelievi raggiunto
            contoRisparmio.doMovimento(new Movimento(TipoMovimento.prelievo, 30.0));
        } catch (IllegalArgumentException e) {
            System.out.println("Errore: " + e.getMessage());
        }

        // Calcolo interessi
        double interessi = contoRisparmio.calcolaInteresse();
        System.out.println("Interesse maturato: " + interessi);

        // Stampa dettagli conto risparmio
        System.out.println(contoRisparmio.toString());
    }
}
