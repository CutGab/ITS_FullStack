package Esercizi.Esercizi_prova;

import java.util.Scanner;

public class Es_3 {

    public static void main(String[] args) {
        
        Scanner myObj = new Scanner(System.in);

        System.out.println("Inserire il numero che desidera: ");

        int n = myObj.nextInt();

        int result = n;

        for (int i =  1; i <= n - 1; i++) {

            result *= i;

        }

        System.out.println(result);
    }
    
}
