from animal import animal

class sea_creature(animal):
    def __init__(self, name, species, food, lowest_depth):  # lowest_depth in meters
        animal.__init__(self, name, species, food)
        self.lowest_depth = lowest_depth
        
    def __repr__(self):
        return "\033[94m{}\033[0m-{}: sea_creature, lowest depth = {} meters".format(self.name, self.species, self.lowest_depth)