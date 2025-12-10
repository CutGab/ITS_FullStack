package Esercizi.Esercizi_Prova;

import java.util.Scanner;

public class Es_2 {

    public static void main(String[] args) {

        Scanner myObj = new Scanner(System.in);

        System.out.println("Inserisci il primo numero: ");

        int k = myObj.nextInt();

        System.out.println("Inserisci il secondo numero: ");

        int n = myObj.nextInt();

        int sommatoria = 0;
        int power = 1;

        for (int i = 1; i <= n; i ++) {

            power = power * k;

            sommatoria += power;
        }

        System.out.println(sommatoria);
    }
    
}
