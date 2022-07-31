from .animal import Animal
from movements import Walking, Swimming

class Seal(Animal, Walking, Swimming):
    """Creates the seal class
    """
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)


    def __str__(self):
        """function to show animal name and species
        Returns:
            string: that describes the animal
        """
        return f"{self.name} is a {self.species}"
