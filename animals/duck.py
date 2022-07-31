from .animal import Animal
from movements import Walking, Swimming


class Duck(Animal, Walking, Swimming):
    """Creates the duck class, inherting from the Animal, Walking, and Swimming classes, do not use super().__init__ when using multiple classes
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

    def quack(self):
        print("The duck quacks. A lot")
