from Ride import Ride

class Park:

    def __init__(self, rides: dict[str, Ride]):
        self.rides = rides

    def add(self, ride: Ride):
        if ride.id not in self.rides:
            self.rides[ride.id] = ride

    def get(self, ride_id):
        return self.rides[ride_id]
    
    def list_all(self):

        rides: list = []

        for values in self.rides.values():

            rides.append(values)

        return rides
