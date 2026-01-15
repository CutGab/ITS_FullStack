package Esercizi.Esercizi_Classi.BankAccount;

import java.util.ArrayList;

public class ContiCorrenti {

    private String intestatario;
    private int numero;
    private double saldo;
    private ArrayList<Movimento> movimenti;

    public ContiCorrenti(String intestatario, int numero) {
        this.intestatario = intestatario;
        this.numero = numero;
        this.saldo = 0.0;
        this.movimenti = new ArrayList<>();
   }

    public ContiCorrenti(String intestatario, int numero, double depositoIniziale) {
        this.intestatario = intestatario;
        this.numero = numero;
        this.movimenti = new ArrayList<>();
        if (depositoIniziale > 0) {
            doMovimento(new Movimento (TipoMovimento.versamento, depositoIniziale));
        }

    }

    public double getSaldo() {
        return saldo;
    }

    public Movimento doMovimento(Movimento mioMovimento) {

        if (mioMovimento.getTipo_mov() == TipoMovimento.prelievo) {
            if (mioMovimento.getImporto() > this.saldo) {
                throw new IllegalArgumentException("Importo troppo grande!");
            }

            this.saldo -= mioMovimento.getImporto();
            movimenti.add(mioMovimento);

        } else {

            if (mioMovimento.getTipo_mov() == TipoMovimento.versamento) {
                if (mioMovimento.getImporto() < 0) {
                    throw new IllegalArgumentException("Versamento Impossibile!");
                }

                this.saldo += mioMovimento.getImporto();
                movimenti.add(mioMovimento);
            }
        }

        return mioMovimento;
    }

    public boolean CheckBalance() {

        double saldo_fittizio = 0.00;

        for (Movimento movimento : movimenti) {

            if (movimento.getTipo_mov() == TipoMovimento.prelievo) {
                saldo_fittizio -= movimento.getImporto();
            } else {
                saldo_fittizio += movimento.getImporto();
            }
        }

        if (saldo_fittizio == this.saldo) {
            return true;
        }
        return false;
    }

    public String showContoDetails() {
        StringBuilder sb = new StringBuilder();

        sb.append("Intestatario: ").append(intestatario).append("\n")
          .append("Numero conto: ").append(numero).append("\n")
          .append("Saldo attuale: ").append(saldo).append("\n")
          .append("Movimenti:\n");

        for (Movimento m : movimenti) {
            sb.append("- ").append(m.getTipo_mov()).append(" : ")
              .append(m.getImporto()).append("\n");
        }

        return sb.toString();
    }
}
