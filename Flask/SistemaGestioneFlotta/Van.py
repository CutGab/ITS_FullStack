from Veichle import *

class Van(Veichle):

    def __init__(self, plate_id, model, driver_name, registration_year, status, max_load_kg: int, require_special_license: bool):
        super().__init__(plate_id, model, driver_name, registration_year, status)

        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self):
        return "Van"
    
    def base_cleaning_time(self):
        return 60
    
    def wear_level(self):
        return 4
    
    def info(self):
        
        base_info = super().info()
        
        base_info.update({
            "Carico Massimo": self.max_load_kg,
            "Licensa Necessaria": self.require_special_license
        })
        
        return base_info