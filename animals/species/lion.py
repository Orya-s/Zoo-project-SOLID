from food import food
from animals.mammal import mammal

class lion(mammal):
    def __init__(self, name, species="lion", food=food("meat", 6, "kg"), preg_duration=4):
        mammal.__init__(self, name, species, food, preg_duration)