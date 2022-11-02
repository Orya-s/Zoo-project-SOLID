from ..mammal import mammal
from ..food import food

class lion(mammal):
    def __init__(self, name, species="lion", food=food("meat", 6, "kg"), preg_duration=12):
        super().__init__(name, species, food, preg_duration)