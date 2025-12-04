// Scrivere una classe java con il metodo main che calcola quante ore e quanti minuti mancano alla fine della lezione

// Versione 1: assumere che la lezione termina alle 18.00
// Versione 2: consentire all’utente di inserire l’orario di uscita (acquisendo le ore e i minuti con 2 letture separate)

// Nota: utilizzare 2 oggetti di tipo java.util.Date


package Esercizi.Esercizi_Oggetti.Es_Date;

import java.util.Date;
import java.util.Scanner;

public class Es_1_VER2 {

    public static void main(String[] args) {

        Date orario_fine = new Date();
        orario_fine.setHours(18);
        orario_fine.setMinutes(0);
        Date orario_utente = new Date();
        
        Scanner src = new Scanner(System.in);

        System.out.println("Inserire l'orario di uscita (ore): ");
        orario_utente.setHours(src.nextInt());

        System.out.println("Inserire l'orario di uscita (minuti): ");
        orario_utente.setMinutes(src.nextInt());

        long mills = (orario_fine.getTime() - orario_utente.getTime());

        long diffMinutes = (mills / (1000 * 60)) % 60;
        long diffHours = mills / (1000 * 60 * 60);

        System.out.printf("Mancano Ore %d, Minuti %d", diffHours, diffMinutes);

    }

}
