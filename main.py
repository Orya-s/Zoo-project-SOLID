from zoo import Zoo
from init_zoo import init

# creating my zoo
zoo = Zoo()
init(zoo)

# 2 weeks simulation:
NUM_DAYS = 14

for day in range(NUM_DAYS):
    zoo.feed_all()

print(zoo)