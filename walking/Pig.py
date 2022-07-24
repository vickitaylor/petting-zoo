from datetime import date

class Pig:
    """creates the Pig class
    """
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
