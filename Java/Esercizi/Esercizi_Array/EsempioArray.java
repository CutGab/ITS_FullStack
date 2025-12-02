package Esercizi.Esercizi_Array;

import java.util.Scanner;

public class EsempioArray {

    public static void main(String[] args) {
        int[] array = new int[5];
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < array.length; i++) {
            System.out.println("Inserisci un numero intero: ");
            array[i] = sc.nextInt();
        }

        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }

        char[] nome = {'a', 'n', 'n', 'a'};
        System.out.println(nome.length);
        // nome.length = 12; // NON compila

        for (char c : nome) {
            System.out.println(c);
        }
    }
}
