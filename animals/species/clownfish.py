from food import food
from animals.sea_creature import sea_creature

class clownfish(sea_creature):
    def __init__(self, name, species="clownfish", food=food("algae", 3, "grams"), lowest_depth=15):
        sea_creature.__init__(self, name, species, food, lowest_depth)