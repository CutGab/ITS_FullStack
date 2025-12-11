// Scrivere un programma che legge una stringa da tastiera e indica se la stringa inserita è palindroma, cioè se contiene la stessa sequenza di caratteri leggendola da destra e da sinistra.
// Tecnica risolutiva:
// Creazione di una copia invertita della stringa
// Esempi di stringhe palindrome:
// anna >> palindromo
// itopinonavevanonipoti >> palindromo

package Esercizi.Esercizi_Stringhe;

import java.util.Scanner;

public class Es_3 {

    public static void main(String[] args) {

        String stringa_inversa = "";
        
        Scanner src = new Scanner(System.in);

        System.out.println("Inserire una stringa: ");
        String str = src.nextLine();

        for (int i = 0; i < str.length(); i++) {

            stringa_inversa = str.toLowerCase().charAt(i) + stringa_inversa;
            
        }

        System.out.println("Palindromo: " + stringa_inversa.equals(str.toLowerCase()));
    }
    
}
