// Esercizio n. 4 – somma elementi array
// Creare un array A di n numeri interi e popolarlo dinamicamente.
// Calcolare e stampare:
// la somma di tutti gli elementi
// la somma degli elementi di posto pari (il posto zero viene contato nei pari!)
// la somma degli elementi di posto dispari
// la media aritmetica di tuti gli elementi


package Esercizi.Esercizi_Array;

import java.util.Scanner;

public class Es_4 {

    public static void main(String[] args) {
        
        int [] array = new int [5];

        double somma = 0;
        int somma_pari = 0;
        int somma_dispari = 0;

        Scanner src = new Scanner(System.in);

        for (int i = 0; i < array.length; i++) {

            System.out.println("Inserisci un nuovo numero: ");
            array[i] = src.nextInt();
        }

        for (int i = 0; i < array.length; i++) {

            somma += array[i];
            
        }

        for (int i = 0; i < array.length; i++) {

            if (i % 2 == 0) {
                somma_pari += array[i];
            } else {
                somma_dispari += array[i];
            }
            
        }

        System.out.println("La somma equivale a " + somma);
        System.out.println("La somma dei numeri pari equivale a " + somma_pari);
        System.out.println("La somma dei numeri dispari equivale a " + somma_dispari);
        System.out.println("La media equivale a " + somma/array.length);
        
    }    
}
