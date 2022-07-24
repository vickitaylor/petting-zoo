from datetime import date

class Llama:
    """ creating the Llama class with 4 parameters
    """
    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        """string to show when they ate when the function is called
        """
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        """function to show animal name and species
        Returns:
            string: that describes the animal
        """
        return f"{self.name} is a {self.species}."
