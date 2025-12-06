from Ride import Ride

class Rollercoaster(Ride):

    def __init__(self, id, nome, min_height_cm, inversions: int):
        super().__init__(id, nome, min_height_cm)

        self.inversions = inversions

    
    def category(self):
        return "Roller_coaster"
    
    def base_wait(self):
        return 40
    
    def info(self):
        return {"Id": self.id, "Nome": self.nome, "Altezza minima": self.min_height_cm, "Categoria": self.category(), "Inversioni": self.inversions}
