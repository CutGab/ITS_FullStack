public class Test {

    public static void main(String[] args) {
        
        Tamagotchi t = new Tamagotchi("Fido", "Cane");

        System.out.println(t.getSpecies());

        t.setEnergy(20); //Output atteso: Non deve funzionare

        t.mangia();

        System.out.println(t.getEnergy());
        System.out.println(t.getWeight());

        t.gioca();

        System.out.println(t.getEnergy());
        System.out.println(t.getWeight());
        
    }    
}
