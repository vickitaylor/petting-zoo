from datetime import date

class Llama:
    """ creating the Llama class with 3 parameters
    """
    def __init__(self, name, species, shift):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
