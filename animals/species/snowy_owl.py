from food import Food
from animals.bird import Bird

class SnowyOwl(Bird):
    def __init__(self, name, species="snowy owl", food=Food("worms", 100, "grams"), wing_span=52):
        Bird.__init__(self, name, species, food, wing_span)