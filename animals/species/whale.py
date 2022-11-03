from food import food
from animals.mammal import mammal
from animals.sea_creature import sea_creature

class whale(mammal, sea_creature):
    def __init__(self, name, species="whale", food=food("plankton ", 2000, "kg"), preg_duration=14, lowest_depth=3000):
        mammal.__init__(self, name, species, food, preg_duration)
        sea_creature.__init__(self, name, species, food, lowest_depth)