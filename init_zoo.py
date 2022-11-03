from animals.species.lion import Lion
from animals.species.whale import Whale
from animals.species.goose import Goose
from animals.species.snowy_owl import SnowyOwl
from animals.species.clownfish import Clownfish


def init(zoo):
    Simba = Lion("Simba")
    Nala = Lion("Nala")
    Willy = Whale("Willy")
    Akka = Goose("Akka")
    Hedwig = SnowyOwl("Hedwig")
    Nemo = Clownfish("Nemo")
    Marlin = Clownfish("Marlin")

    animals = [Simba, Nala, Willy, Akka, Hedwig, Nemo, Marlin]
    zoo.add_animals(animals)