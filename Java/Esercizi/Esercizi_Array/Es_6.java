// Esercizio n. 6 - inversione array vers.2
// Letto in input un array A di n numeri interi, invertire l’ordine degli elementi.
// NB: utilizzare il SOLO array iniziale.
// Esempio: se A è (10,27,13, 4), allora devo ottenere A (4,13,27,10)
// Al termine dell’elaborazione stampare l'array A.


package Esercizi.Esercizi_Array;

import java.util.Scanner;

public class Es_6 {
    
    public static void main(String[] args) {
        
        Scanner src = new Scanner(System.in);
        
        int [] array = new int [5];


        for (int i = 0; i < array.length; i++) {
            
            System.out.println("Inserisci un numero: ");
            array[i] = src.nextInt();
            
        }

        for (int i = 0; i < array.length; i++) {

            int last_num = array[array.length - 1 - i];

            int temp = array[i];

            array[i] = last_num;
            
        }

        for (int i = 0; i < array.length; i++) {

            System.out.println(array[i]);
        }
    }
}
