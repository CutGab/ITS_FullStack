// Esercizio n. 1 – copia array
// Letto in input un array A di n numeri interi, creare un secondo array della stessa dimensione e popolarlo copiando tutti gli elementi del primo

package Esercizi.Esercizi_Array;

import java.util.Scanner;

public class Es_1 {
    public static void main(String[] args) {
        
        Scanner src = new Scanner(System.in);
        
        int [] array = new int [5];

        int[] array2= new int[5];

        for (int i = 0; i < array.length; i++) {
            
            System.out.println("Inserisci un numero: ");
            array[i] = src.nextInt();
            
        }

        for (int i = 0; i < array2.length; i++) {

            array2[i] = array[i];
            
        }

        for (int i = 0; i < array2.length; i++) {

            System.out.println(array2[i]);
            
        }
        
    }
    
}
