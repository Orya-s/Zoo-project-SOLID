from food import Food
from animals.mammal import Mammal
from animals.sea_creature import SeaCreature

class Whale(Mammal, SeaCreature):
    def __init__(self, name, species="whale", food=Food("plankton", 2000, "kg"), preg_duration=14, lowest_depth=3000):
        Mammal.__init__(self, name, species, food, preg_duration)
        SeaCreature.__init__(self, name, species, food, lowest_depth)
        
    def __repr__(self):
        return "\033[94m{}\033[0m-{}: mammal & sea_creature, pregnancy duration = {} months, lowest depth = {} meters".format(self.name, self.species, self.preg_duration, self.lowest_depth)