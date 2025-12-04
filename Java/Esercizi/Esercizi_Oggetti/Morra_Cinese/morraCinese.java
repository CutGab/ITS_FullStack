// Scrivere una classe MorraCinese con il metodo main che simuli una partita alla Morra Cinese tra il computer e un giocatore.
// Il sistema genera la sua mossa estraendo casualmente un valore tra 0, 1, 2 che corrisponderanno a sasso, carta, forbici.
// A questo punto il giocatore esegue il suo lancio digitando 0,1,2 (con la stessa corrispondenza di prima).
// La regola è che forbici vince su carta, carta vince su sasso, sasso vince su forbici.

// Dopo ogni scontro vengono stampati i tiri del sistema e del giocatore e infine viene mostrato l’esito di chi vince. 
// In caso di stesso tiro, si considera pareggio. 
// A questo punto viene richiesto se giocare ancora oppure uscire dal gioco.



package Esercizi.Esercizi_Oggetti.Morra_Cinese;

import java.util.Random;
import java.util.Scanner;

public class morraCinese {

    public static void main(String[] args) {

        Random rand = new Random();
        Scanner src = new Scanner(System.in);
        String answer = "y";

        while (answer != "n") {

            int opponent_move = rand.nextInt(0, 3);

            System.out.println("Sasso (0), Carta(1) o Forbice(2)?: ");
            int move = src.nextInt();

            if (move == 0) {

                if (opponent_move == 1) {
                    System.out.println("Carta! Hai perso.");

                } else if (opponent_move == 2) {
                    System.out.println("Forbice! Hai vinto!");

                } else if (opponent_move == 0) {
                    System.out.println("Sasso! Pareggio.");
                }
            }

            if (move == 1) {

                if (opponent_move == 1) {
                    System.out.println("Carta! Pareggio.");

                } else if (opponent_move == 2) {
                    System.out.println("Forbice! Hai perso!");

                } else if (opponent_move == 0) {
                    System.out.println("Sasso! Hai vinto!");
                    break;
                }
            }

            if (move == 2) {

                if (opponent_move == 1) {
                    System.out.println("Carta! Hai vinto!.");
                    break;

                } else if (opponent_move == 2) {
                    System.out.println("Forbice! Pareggio!");

                } else if (opponent_move == 0) {
                    System.out.println("Sasso! Hai perso.");
                }
                
            }
            
            System.out.println("Vuoi continuare a giocare? (Y/N): ");
            answer = src.next().toLowerCase();
            
            if (!answer.equals("y")) {
                break;
            }

        }

    }
}
