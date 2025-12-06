from Ride import Ride

class Carousel(Ride):

    def __init__(self, id, nome, min_height_cm, animali: list):
        super().__init__(id, nome, min_height_cm)

        self.animali = animali

    
    def category(self):
        return "Family"
    
    def base_wait(self):
        return 10
    
    def info(self):
        return {"Id": self.id, "Nome": self.nome, "Altezza minima": self.min_height_cm, "Categoria": self.category(), "Animali": self.animali}
