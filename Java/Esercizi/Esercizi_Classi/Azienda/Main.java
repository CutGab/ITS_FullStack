package Esercizi.Esercizi_Classi.Azienda;

import java.util.Date;

public class Main {

    public static void main(String[] args) {

        System.out.println(Impiegato.getContatore());

        Impiegato imp1 = new Impiegato("Mirko", 1500, new Date());

        System.out.println(imp1);
        System.out.println(Impiegato.getContatore());

        Impiegato imp2 = new Impiegato("Dioni", 1501, new Date());
        
        System.out.println(imp2);
        System.out.println(Impiegato.getContatore());

        imp1.incrementaSalario(100);
        System.out.println(imp1);

        imp2.incrementaSalario(0.01);
        System.out.println(imp2);

        Azienda azienda = new Azienda("eng");
        System.out.println(azienda);
        azienda.assume(imp1);
        azienda.assume(imp2);
        System.out.println(azienda);

        azienda.incrementaSalarioxTutti(50);

        System.out.println(azienda);

        Manager m1 = new Manager("man1", 30000, new Date(),"Anna");
        Manager m2 = new Manager("man2", 30000, new Date(115,1,1),"Anna");

        System.out.println(m1);
        System.out.println(m2);

        m1.incrementaSalario(100);
        m2.incrementaSalario(100);

        System.out.println("dopo l'aumento...");
        System.out.println(m1);
        System.out.println(m2);

    }
    
}

