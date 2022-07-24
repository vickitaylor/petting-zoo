class SnakePit:
    """class to create the snake pit
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
