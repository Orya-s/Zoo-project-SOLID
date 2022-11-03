from animals.species.lion import lion
from animals.species.whale import whale
from animals.species.goose import goose
from animals.species.snowy_owl import snowy_owl
from animals.species.clownfish import clownfish


def init(zoo):
    Simba = lion("Simba")
    Nala = lion("Nala")
    Willy = whale("Willy")
    Akka = goose("Akka")
    Hedwig = snowy_owl("Hedwig")
    Nemo = clownfish("Nemo")
    Marlin = clownfish("Marlin")

    animals = [Simba, Nala, Willy, Akka, Hedwig, Nemo, Marlin]
    zoo.add_animals(animals)
    # zoo.print_zoo()