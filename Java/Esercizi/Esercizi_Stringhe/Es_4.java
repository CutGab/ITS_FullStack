// Scrivere un programma in cui, dati in input una stringa e un carattere, viene stampato il numero di occorrenze del carattere nella stringa
// Scrivere 2 implementazioni, usando le seguenti tecniche:
// Usare il metodo charAt(int)
// Usare il metodo indexOf(char, int)

// Esempio 
// aaabbbccc , b  >> 3 occorrenze
// aaabbbccc , x  >> 0 occorrenze
// abcabcabc , a  >> 3 occorrenze

package Esercizi.Esercizi_Stringhe;

import java.util.Scanner;

public class Es_4 {

    public static void main(String[] args) {

        Scanner src = new Scanner(System.in);

        System.out.println("Inserire una stringa: ");
        String stringa = src.nextLine();

        System.out.println("Inserire un carattere: ");
        char carattere = src.next().charAt(0);

        Integer occorrenze = 0;

        for (int i = 0; i < stringa.length(); i++) {

            if (stringa.charAt(i) == carattere) {
                occorrenze ++;
            }
            
        }

        System.out.printf("Occorrenze di %s sono %d", carattere, occorrenze);

    }
    
}
