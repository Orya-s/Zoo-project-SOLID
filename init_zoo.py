from animals.species.lion import lion


def init(zoo):
    Simba = lion("Simba")
    Nala = lion("Nala")

    animals = [Simba, Nala]
    zoo.add_animals(animals)
    zoo.print_zoo()