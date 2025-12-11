// Il programma legge una stringa da tastiera e controlla se il testo inserito è composto solo da cifre o se sono presenti anche delle lettere.
// NB: un carattere c è una cifra se c >= ‘0’ && c <=‘9’
// Stampa a video 
// “testo numerico” oppure “testo NON numerico”.


package Esercizi.Esercizi_Stringhe;

import java.util.Scanner;

public class Es_1 {

    public static void main(String[] args) {
        
        Scanner scr = new Scanner(System.in);
        int lettere = 0;
        int numeri = 0;


        System.out.println("Inserisci una stringa:");
        String str = scr.nextLine();

        for (int i = 0; i < str.length(); i++) {

            if(Character.isDigit(str.charAt(i))) {

                numeri ++;
            }

            else {
                lettere ++;
            }
            
        }

        if (lettere > 0 && numeri > 0) {
            System.out.println("Testo non numerico");
        }

        else if (lettere > 0 && numeri == 0) {
            System.out.println("Testo non numerico");
        }

        else if (lettere == 0 && numeri > 0) {
            System.out.println("Testo numerico");
        }
        
    }    
}
