from zoo import zoo
from food import food

class animal:
    def __init__(self, name, species, food:food):
        self.name = name 
        self.species = species
        self.food = food    
        zoo.add_animal(self)
        
    def eat(self):
        zoo.feed_animal(self.food.get_type(), self.food.get_amount())
    
    def get_food(self):
        return self.food
    
    
        
    