from Veichle import *

class Car(Veichle):

    def __init__(self, plate_id, model, driver_name, registration_year, status, doors: int, is_cabrio: bool):
        super().__init__(plate_id, model, driver_name, registration_year, status)

        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self):
        return "Car"
    
    def base_cleaning_time(self):
        return 30
    
    def wear_level(self):
        return 1
    
    def info(self):
        
        base_info = super().info()
        
        base_info.update({
            "Numero Porte": self.doors,
            "Cabrio": self.is_cabrio
        })
        
        return base_info
