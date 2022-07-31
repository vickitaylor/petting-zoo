class Attraction():
    """ Defines the attraction class.
    """

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        """function that will add an animal to the "empty" animal list

        Args:
            animal (dict): adds the animal dictionary to the list
        """
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.attraction_name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)

    @property
    def last_critter_added(self):
        return f'The last critter added to the {self.attraction_name} was {self.animals[-1]}'
