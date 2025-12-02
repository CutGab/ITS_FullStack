// Esercizio n. 3 - copia metà array
// Creare un array A di n numeri interi, popolarlo dinamicamente SOLO per metà e stamparlo. Popolare poi la seconda metà con gli stessi valori della prima e stampare nuovamente.
// NB: per semplicità assumiamo che la dimensione dell’array sia un numero pari.
// Es. creo un array da 10 elementi e lo popolo con questi 5 valori (3, 5, 8, 2, 4).  Alla fine l'array deve diventare (3, 5, 8, 2, 4, 3, 5, 8, 2, 4).


package Esercizi.Esercizi_Array;

import java.util.Scanner;

public class Es_3 {

    public static void main(String[] args) {

        int [] array = new int [10];

        Scanner src = new Scanner(System.in);

        for (int i = 0; i < array.length / 2; i++) {
            System.out.println("Inserisci un numero: ");
            array[i] = src.nextInt();
        }

        for (int i = 0; i < array.length / 2; i++) {
            array[i + array.length / 2] = array[i];
        }

        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
    }
}
