package Esercizi_Classi.Es_1;

public class Persona {

    //1. Attributi
    private String name;
    private int age;
    private double weight;

    //2. Costruttori
    public Persona(String name, int age, double weight) {
        this.name = name;
        this.age = age;
        this.weight = weight;
    }

    public Persona(String name, double weight) {
        this.name = name;
        this.weight = weight;
        this.age = 0; //this non necessario quando non viene dichiarato nel costruttore
    }

    public String getName() {
        return name;
    }    

    public int getAge() {
        return age;
    }

    public void setAge(int age) {

        if(age > 0)
            this.age = age;

        else
            System.out.println("Sei una scimmia");
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "Persona [name=" + name + ", age=" + age + ", weight=" + weight + "]";
    }

    //metodi operativi

    public void cresce() {

        age++;    
    }

    public void cresce(int incremento) {

        age += incremento;    
    }

}
