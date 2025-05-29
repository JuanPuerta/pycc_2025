# Defining a satellite class

class Satellite:
    def __init__(self, name, altitude, orbit_type="LEO"):
        self.name = name
        self.altitude = altitude  # in kilometers
        self.orbit_type = orbit_type
        self.status = "Idle"
        self.data_collected = 0 # in GB