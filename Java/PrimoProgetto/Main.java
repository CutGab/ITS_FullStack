package PrimoProgetto;

public class Main {
    public static void main(String[] args) {

        String spazio = "\n\n";
        boolean flag = false;

        somma(5, 10);

        System.out.print(spazio);

        for (int i = 10; i != 0; i--) {

            System.out.print(i + ", ");
        }

        etichetta: 
        for(int i = 0; i < 20; i++){
            for(int j = 0; j < 10; j++){
                if(i==12 && j==5)
                    continue etichetta;
                System.out.println(j);
            }
            System.out.println(" -- " + i);
        } 

        
        System.out.print(spazio);

        if (flag) {
            System.out.print("È tutto vero");
        }

        else {
            System.out.print("È tutto falso");
        }
    }

    static void somma (int x, int y) {
        
        int somma = x + y;
        System.out.printf("La somma tra %d e %d è di %d", x, y, somma);
    }
    
}
