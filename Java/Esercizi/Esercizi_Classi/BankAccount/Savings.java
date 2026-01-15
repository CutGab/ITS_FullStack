package Esercizi.Esercizi_Classi.BankAccount;

public class Savings extends ContiCorrenti {

    private double interessi;
    private int max_prel_gg;

    public Savings(String intestatario, int numero, double interessi, int max_prel_gg) {
        super(intestatario, numero);
        this.interessi = interessi;
        this.max_prel_gg = 3;
    }

    public Savings(String intestatario, int numero, double depositoIniziale, double interessi, int max_prel_gg) {
        super(intestatario, numero, depositoIniziale);
        this.interessi = interessi;
        this.max_prel_gg = 3;
    }

    @Override
    public Movimento doMovimento(Movimento mioMovimento) {
        if (mioMovimento.getTipo_mov() == TipoMovimento.prelievo) {
            if (this.max_prel_gg > 0) {
                this.max_prel_gg--;
                System.out.println("Prelievi rimasti: " + this.max_prel_gg);
                return super.doMovimento(mioMovimento);
            } else {
                throw new IllegalArgumentException("Numero massimo di prelievi giornalieri raggiunto");
            }
        } else if (mioMovimento.getTipo_mov() == TipoMovimento.versamento) {
            return super.doMovimento(mioMovimento);
        } else {
            throw new IllegalArgumentException("Tipo di movimento non valido");
        }
    }

    public double calcolaInteresse() {

       return this.getSaldo() * this.interessi/ 100;


    }

    @Override
    public String toString() {
        String dettagliBase = super.showContoDetails();

        StringBuilder sb = new StringBuilder(dettagliBase);
        sb.append("Interessi: ").append(interessi).append("%\n")
        .append("Prelievi rimanenti oggi: ").append(max_prel_gg).append("\n");

        return sb.toString();
    }


}


