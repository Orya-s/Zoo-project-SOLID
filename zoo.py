from food import food
from animal import animal

class zoo:
    def __init__(self):
        self.animals = []
        self.food_supply = {}   # {"food_type":amount}
        self.restock_amount = 50
        
    def add_animal(self, animal:animal):
        self.animals.append(animal)
        self.add_food(animal.get_food().get_type())
        
    def add_animals(self, animals):
        [self.add_animal(a) for a in animals]
        
    def add_food(self, food:food):
        if food not in self.food_supply:
            self.food_supply[food] = self.restock_amount
            
    def feed_all(self):
        [self.feed_animal(animal.get_food()) for animal in self.animals]    # in feed_animal- recievs food   # map ?
        
    def feed_animal(self, food:food):
        food_type = food.get_type()
        amount = food.get_amount()
        if self.food_supply[food_type] - amount < 0:
            self.restock(food_type)
        self.food_supply[food_type] -= amount
        
    def restock(self, food):
        print("{} ran out, filling the supply...".format(food))
        self.food_supply[food] += self.restock_amount
        
    def print_zoo(self):    # operator overloading __str__ 
        print(self.animals)