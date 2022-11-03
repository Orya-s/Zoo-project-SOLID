from animal import animal

class sea_creature(animal):
    def __init__(self, name, species, food, lowest_depth):  # lowest_depth in meters
        animal.__init__(self, name, species, food)
        self.lowest_depth = lowest_depth