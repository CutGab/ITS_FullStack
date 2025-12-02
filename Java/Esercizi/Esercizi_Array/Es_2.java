// Esercizio n. 2 - inversione array
// Letto in input un array A di n numeri interi, creare un secondo array B della stessa dimensione e popolarlo invertendo l’ordine degli elementi del primo.

package Esercizi.Esercizi_Array;

import java.util.Scanner;

public class Es_2 {
    
    public static void main(String[] args) {
        
        Scanner src = new Scanner(System.in);
        
        int [] array = new int [5];

        int[] array2= new int[5];

        for (int i = 0; i < array.length; i++) {
            
            System.out.println("Inserisci un numero: ");
            array[i] = src.nextInt();
            
        }

        for (int i = 0; i < array2.length; i++) {

            int last_num = array[array.length - 1 - i];

            array2[i] = last_num;
            
        }

        for (int i = 0; i < array2.length; i++) {

            System.out.println(array2[i]);
        }
    }
}
