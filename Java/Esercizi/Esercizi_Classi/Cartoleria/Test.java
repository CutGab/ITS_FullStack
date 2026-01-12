package Esercizi.Esercizi_Classi.Cartoleria;

import java.time.LocalDate;

public class Test {

    public static void main(String[] args) {
        
        Privato p = new Privato("Mario", 200);

        Azienda a = new Azienda("ITS", 1000);

        Gomma g1 = new Gomma("Standler", "NVIDIA", 5, "Rotonda", 30.0, 30.0);

        Penna p1 = new Penna("Bic", "NVIDIA", 10, 10, "Verde");

        Ordine op1 = new Ordine(LocalDate.now(), a);

        op1.addArticolo(p1);
        op1.addArticolo(g1);

        op1.chiudi();

        System.out.println(a);



    }
    
}
