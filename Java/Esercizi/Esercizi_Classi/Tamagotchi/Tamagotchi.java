package Esercizi.Esercizi_Classi.Tamagotchi;
public class Tamagotchi {

    String name;
    String species;
    double weight;
    double height;
    int energy;

    public Tamagotchi(String name, String species) {
        this.name = name;

        switch (species) {
            case "Gatto":
                
                this.weight = 100;
                this.height = 10;

            case "Canarino":
                
                this.weight = 10;
                this.height = 3;

            case "Coniglio":
                
                this.weight = 100;
                this.height = 10;

            default:
                this.species = "Cane";
                this.weight = 300;
                this.height = 20;
        }

        this.energy = 3;
    }

    public Tamagotchi(String name) {
        this.name = name;
        this.species = "Cane";
        this.weight = 300;
        this.height = 20;
        this.energy = 3;
    }

    public String getName() {
        return name;
    }

    public String getSpecies() {
        return species;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public int getEnergy() {
        return energy;
    }

    public void setEnergy(int energy) {

        if (energy >= 1 && energy <= 10) {
            this.energy = energy;
        }
    }

    public boolean mangia () {

        if (energy < 10) {

            height ++;
            weight += 150;
            energy ++;

        }

        return false;

    }

    public boolean dorme() {

        if (energy < 10) {

            energy ++;

        }

        return false;
    }

    public boolean gioca () {
        
        if (weight > 100) {

            weight -= 100;
            energy --;

        }

        return false;

    }

}
