from .animal import Animal
from datetime import date
from movements import Walking, Swimming

class Polarbear(Animal, Walking, Swimming):
    """Creates the polarbear class
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

    def feed(self):
        print(f'on {date.today()}, {self.name} had "Baby Shark" sung to it so it would eat its {self.food}')
