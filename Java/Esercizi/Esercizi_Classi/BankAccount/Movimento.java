package Esercizi.Esercizi_Classi.BankAccount;

import java.time.LocalDateTime;

public class Movimento {

    private final TipoMovimento tipo_mov;
    private final LocalDateTime istante;
    private double importo;
    
    
    public Movimento(TipoMovimento tipo_mov, double importo) {
        this.tipo_mov = tipo_mov;
        this.istante = LocalDateTime.now();
        if (importo > 0) {
            this.importo = importo;
        } else {
            throw new IllegalArgumentException("Errore Importo troppo piccolo!");
        }
    }


    public TipoMovimento getTipo_mov() {
        return tipo_mov;
    }


    public LocalDateTime getIstante() {
        return istante;
    }


    public double getImporto() {
        return importo;
    }


    @Override
    public String toString() {
        return "Movimento [tipo_mov=" + tipo_mov + ", istante=" + istante + ", importo=" + importo + "]";
    }

    

    

    }
