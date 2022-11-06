from animal import Animal

class SeaCreature(Animal):
    def __init__(self, name, species, food, lowest_depth):  # lowest_depth in meters
        Animal.__init__(self, name, species, food)
        self.lowest_depth = lowest_depth
        
    def __repr__(self):
        return super().__repr__() + ": sea_creature, lowest depth = {} meters".format( self.lowest_depth)