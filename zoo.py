from food import food
from animal import animal

class zoo:
    def __init__(self):
        self.animals = []
        self.food_supply = {}   # {"food_type":amount}
        self.restock_amount = {}    # {"food_type":amount}
        self.restock_mul = 5
        
    def add_animal(self, animal:animal):
        self.animals.append(animal)
        self.add_food(animal.get_food())
        
    def add_animals(self, animals):
        [self.add_animal(a) for a in animals]
        
    def add_food(self, food:food):
        food_type = food.get_type()
        if food_type not in self.food_supply:
            self.restock_amount[food_type] = food.get_amount() * self.restock_mul
            self.food_supply[food_type] = self.restock_amount[food_type]
            
    def feed_all(self):
        [self.feed_animal(animal.get_food()) for animal in self.animals]    # in feed_animal- recievs food   # map ?
        
    def feed_animal(self, food:food):
        food_type = food.get_type()
        amount = food.get_amount()
        if self.food_supply[food_type] - amount < 0:
            self.restock(food_type)
        self.food_supply[food_type] -= amount
        
    def restock(self, food_type):
        print("{} ran out, filling the supply...".format(food_type))
        self.food_supply[food_type] += self.restock_amount[food_type]
        
    def print_zoo(self):    # operator overloading __str__ 
        print(self.animals)