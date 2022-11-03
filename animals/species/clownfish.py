from food import Food
from animals.sea_creature import SeaCreature

class Clownfish(SeaCreature):
    def __init__(self, name, species="clownfish", food=Food("algae", 3, "grams"), lowest_depth=15):
        SeaCreature.__init__(self, name, species, food, lowest_depth)