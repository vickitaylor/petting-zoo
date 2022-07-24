from datetime import date

class Llama:
    """Creates the Llama class
    """
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        """string to show when they ate
        """
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        """function to show animal name and species
        Returns:
            string: that describes the animal
        """
        return f"{self.name} is a {self.species}."
