from datetime import date

class Duck:
    """Creates the duck class
    """
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
