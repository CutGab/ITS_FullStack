package Esercizi.Esercizi_prova;

import java.util.Scanner;

public class Es_1 {

    public static void main(String[] args) {
        
        Scanner myObj = new Scanner(System.in);
        
        System.out.println("Insert first number: ");

        int n = myObj.nextInt();

        System.out.println("Inserire il secondo numero: ");

        int k = myObj.nextInt();

        int result = 1;

        for (int power = k; power != 0; power--) {

            result = result * n;

        }

        System.out.println(result);
    }
    
}
