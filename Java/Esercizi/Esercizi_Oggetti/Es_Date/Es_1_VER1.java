// Scrivere una classe java con il metodo main che calcola quante ore e quanti minuti mancano alla fine della lezione

// Versione 1: assumere che la lezione termina alle 18.00
// Versione 2: consentire all’utente di inserire l’orario di uscita (acquisendo le ore e i minuti con 2 letture separate)

// Nota: utilizzare 2 oggetti di tipo java.util.Date


package Esercizi.Esercizi_Oggetti.Es_Date;

import java.util.Date;

public class Es_1_VER1 {

    public static void main(String[] args) {

        Date orario_fine = new Date();
        orario_fine.setHours(19);
        orario_fine.setMinutes(0);
        Date orario_utente = new Date();

        long mills = (orario_fine.getTime() - orario_utente.getTime());

        long diffMinuti = (mills / (1000 * 60)) % 60;
        long diffOre = mills / (1000 * 60 * 60);

        System.out.printf("Mancano Ore %d, Minuti %d", diffOre, diffMinuti);

    }

}