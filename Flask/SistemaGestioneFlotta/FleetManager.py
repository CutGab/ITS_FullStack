from Van import *
from Car import *

class FleetManager:

    def __init__(self, vehicles: dict):
        self.vehicles = vehicles

    def add(self, vehicle: Veichle) -> bool:

        if vehicle.plate_id not in self.vehicles:
            self.vehicles[vehicle.plate_id] = vehicle
            return True
        
        return False

    def get(self, plate_id: str) -> Veichle:

        if plate_id in self.vehicles:
            return self.vehicles[plate_id]
    
    def update(self, plate_id: str, new_vehicle: Veichle) -> None:
        
        if plate_id in self.vehicles:
            self.vehicles.update({plate_id: new_vehicle})
    
    def patch_status(self, plate_id: str) -> None:

        if plate_id in self.vehicles:

            self.vehicles[plate_id].status = plate_id

    def delete(self, plate_id: str):

        if plate_id in self.vehicles:
            self.vehicles.__delitem__(plate_id)

    def list_all(self):

        veicoli = []

        for vehicle in self.vehicles.values():
            veicoli.append(vehicle.info())

        return veicoli
