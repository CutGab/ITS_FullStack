package Esercizi_Classi.Es_1;

public class Test {

    public static void main(String[] args) {
        
        Persona p = new Persona("Mario", 25, 80);

        // System.out.printf("Nome: %s%n", p.name);
        // System.out.printf("Età: %d%n", p.age);
        // System.out.printf("Peso: %.2f%n", p.weight);

        System.out.println(p.getAge());

        p.cresce(40);

        System.out.println(p.toString());
    }
    
}
