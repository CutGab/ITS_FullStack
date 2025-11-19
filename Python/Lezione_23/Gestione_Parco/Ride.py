from abc import ABC, abstractmethod

class Ride(ABC):

    def __init__(self, id: str, nome: str, min_height_cm: int):
        self.id = id
        self.nome = nome
        self.min_height_cm = min_height_cm

    @abstractmethod
    def category(self):
        pass

    @abstractmethod
    def base_wait(self):
        pass

    def info(self):
        return {"Id": self.id, "Nome": self.nome, "Altezza minima": self.min_height_cm, "Categoria": self.category()}
    
    def wait_time(self, crowd_factor: float = 1.0):

        tempo_attesa = self.base_wait() * crowd_factor

        return round(tempo_attesa) 