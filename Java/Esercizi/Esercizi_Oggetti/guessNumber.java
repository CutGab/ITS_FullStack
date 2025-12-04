// Realizzare una classe col main nella quale si estrae randomicamente un numero tra 1 e 10 e l’utente deve indovinarlo.
// L’utente inserisce il numero e il sistema gli risponde una di queste frasi:
// Troppo piccolo, riprova con un numero maggiore
// Troppo grande, riprova con un numero minore
// Esatto! Hai indovinato con N tentativi 
// Il sistema infatti calcola e memorizza il numero di tentativi e lo stampa alla fine
// Note: per l’estrazione casuale usare java.util.Random


package Esercizi.Esercizi_Oggetti;

import java.util.Random;
import java.util.Scanner;

public class guessNumber {

    public static void main(String[] args) {

        int tries = 0;
        
        Random rand = new Random();

        int n = rand.nextInt(1, 11);

        Scanner src = new Scanner(System.in);

        int guess = 0;


        while (guess != n) {

            System.out.println("Inserire il numero che pensi sia uscito: ");
            guess = src.nextInt();

            if (guess > n) {
                System.out.println("Troppo grande, riprova con un numero minore");
                tries++;
            }

            if (guess < n) {
                System.out.println("Troppo piccolo, riprova con un numero maggiore");
                tries++;
            }

            if (guess == n) {
                System.out.printf("Esatto! Hai indovinato con %d tentativi", tries);

            }
            
        }


        
    }
    
}
