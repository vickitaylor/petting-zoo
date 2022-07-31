from .attraction import Attraction


class SnakePit(Attraction):
    """class to create the snake pit
    """

    def __init__(self, name, description):
        super().__init__(name, description)
