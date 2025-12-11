// Il programma legge una stringa da tastiera e la deve interpretare come una data. 
// Il formato dovrà essere GG/MM/AAAA (non eseguire controlli sul formato)
// A questo punto ne estrae i vari campi (giorno, mese ed anno) convertendoli in formato numerico ed infine stampa a video i risultati.

// Il mese deve essere stampato in formato testuale:
// 1 sarà Gennaio ,  2  sarà Febbraio, e cosi via 


package Esercizi.Esercizi_Stringhe;

import java.util.Scanner;

public class Es_2 {

    public static void main(String[] args) {
        
        Scanner src = new Scanner(System.in);
        
        System.out.println("Inserire una stringa in formato GG/MM/AA: ");
        String data = src.nextLine();

        String giorno = data.substring(0, 2);
        int mese = Integer.parseInt(data.substring(3, 5));
        String mese_formattato = "";
        String anno = data.substring(6);

        switch (mese) {
            
            case 1:
                
                mese_formattato += " Gennaio ";
                break;
        
            case 2:
                
                mese_formattato += " Febbraio ";
                break;
        
            case 3:
                
                mese_formattato += " Marzo ";
                break;
        
            case 4:
                mese_formattato += " Aprile ";
                break;

            case 5:
                
                mese_formattato += " Maggio ";
                break;
        
            case 6:
                
                mese_formattato += " Giugno ";
                break;

            case 7:
                
                mese_formattato += " Luglio ";
                break;
        
            case 8:

                mese_formattato += " Agosto ";
                break;

            case 9:
                
                mese_formattato += " Settembre ";
                break;
        
            case 10:

                mese_formattato += " Ottobre ";
                break;

            case 11:
                
                mese_formattato += " Novembre ";
                break;
        
            case 12:

                mese_formattato += " Dicembre ";
                break;
        }

        System.out.println(giorno + mese_formattato + anno);
    }
    
}
