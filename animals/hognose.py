from .animal import Animal
from movements import Slithering

class Hognose(Animal, Slithering):
    """Creates the hognose class
    """
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def __str__(self):
        """function to show animal name and species
        Returns:
            string: that describes the animal
        """
        return f"{self.name} is a {self.species}"
