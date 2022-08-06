from .attraction import Attraction
from movements import Slithering


class SnakePit(Attraction):
    """class to create the snake pit
    """

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.slither_speed > -1:
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(
                f"{animal} doesn't like to be petted, so please do not put it in the {self.attraction_name} attraction.")
