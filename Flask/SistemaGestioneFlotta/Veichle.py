from abc import abstractmethod, ABC

class Veichle(ABC):

    def __init__(self, plate_id: str, model: str, driver_name: str, registration_year: int, status: str):
        self.plate_id = plate_id
        self.model = model
        self.driver_name = driver_name
        self.registration_year = registration_year
        self.status = status


    @abstractmethod
    def vehicle_type(self):
        pass

    @abstractmethod
    def base_cleaning_time(self):
        pass

    @abstractmethod
    def wear_level(self):
        pass

    def info(self):
        return {
            "Id": self.plate_id,
            "Model": self.model,
            "Driver Name": self.driver_name,
            "Vehicle": self.vehicle_type(),
            "Registration Year": self.registration_year,
            "Status": self.status
        }

    
    def estimated_prep_time(self, factor: float = 1.0):

        return int((self.base_cleaning_time() * factor + self.wear_level()) * 15)