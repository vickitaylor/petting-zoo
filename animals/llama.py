from .animal import Animal
from datetime import date
from movements import Walking


class Llama(Animal, Walking):
    """ creating the Llama class with 4 parameters
    """

    def __init__(self, name, species, shift, food, chip_num):
        # Establish the properties of each animal with a default value
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def __str__(self):
        """function to show animal name and species
        Returns:
            string: that describes the animal
        """
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(
            f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')
