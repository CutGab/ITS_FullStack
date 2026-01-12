package Esercizi.Esercizi_Classi.Cartoleria;

import java.util.ArrayList;

public class Magazzino {

    private ArrayList<Articolo> merce;

    public Magazzino() {
        this.merce = new ArrayList<>();
    }

    public void addArticolo(Articolo articolo) {

        if (merce.contains(articolo)) {
            System.out.println("Articolo già in magazzino.");
        } else {
            merce.add(articolo);
        }
    }

    public String showArticoli() {

        String all_articoli = "";

        for (Articolo merce2 : merce) {
            all_articoli += merce2.toString();
        }
        return all_articoli;
        
    }

    public double showTotalCosts () {

        double cost_tot = 0;

        for (Articolo merce2 : merce) {

            cost_tot += merce2.getCosto();
            
        }
        return cost_tot;
    }

    public double showTotalPrices () {

        double prez_tot = 0;

        for (Articolo merce2 : merce) {

            prez_tot += merce2.getPrezzoVendita();
            
        }
        return prez_tot;
    }

    public void ScaricaArticoli(Articolo merce) {
        
    }


    
    
}