// Esercizio n. 5 – stampa zigzag
// Letto in input un array A di n numeri interi, stampare gli elementi a zigzag, cioè il primo e l'ultimo, poi il secondo e il penultimo, e così via.
// NB: assumiamo la dimensione pari.


package Esercizi.Esercizi_Array;

import java.util.Scanner;

public class Es_5 {
    
    public static void main(String[] args) {
        
        int [] array = new int [4];

        Scanner src = new Scanner(System.in);

        for (int i = 0; i < array.length; i++) {

            System.out.println("Inserisci un nuovo numero: ");
            array[i] = src.nextInt();
        }

        for (int i = 0; i < array.length / 2; i++) {

            System.out.println(array[i]);
            System.out.println(array[array.length - 1 - i]);      
        }        
    }    
}
