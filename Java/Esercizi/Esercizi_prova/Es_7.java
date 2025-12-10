package Esercizi.Esercizi_Prova;

import java.util.Date;

public class Es_7 {

    public static void main(String[] args) {
        
        Date d = new Date();

        System.out.println(d);

        System.out.println(d.getDay());

        System.out.println(d);

        d.setMonth(80);

        System.out.println(d);

        Date natale = new Date(125, 11, 25);

        System.out.println(natale);

    }    
}
