from .animal import Animal
from movements import Walking


class Goat(Animal, Walking):
    """Creates the goat class, using the parent class Animal 
    """

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def __str__(self):
        """function to show animal name and species
        Returns:
            string: that describes the animal
        """
        return f"{self.name} is a {self.species}"

    def run(self):
        print(f'{self} runs')
