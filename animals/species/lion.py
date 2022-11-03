from food import Food
from animals.mammal import Mammal

class Lion(Mammal):
    def __init__(self, name, species="lion", food=Food("meat", 6, "kg"), preg_duration=4):
        Mammal.__init__(self, name, species, food, preg_duration)