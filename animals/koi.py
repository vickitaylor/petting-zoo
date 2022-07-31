from .animal import Animal
from movements import Swimming

class Koi(Animal, Swimming):
    """Creates the koi class
    """
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)

    def __str__(self):
        """function to show animal name and species
        Returns:
            string: that describes the animal
        """
        return f"{self.name} is a {self.species}"

    def swims(self):
        print(f'{self} swims like a fish')

    def bubbles(self):
        print("The Koi makes bubbles.")
