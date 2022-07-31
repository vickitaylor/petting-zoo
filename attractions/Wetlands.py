from .attraction import Attraction

class Wetlands(Attraction):
    """class that creates wetland areas in the zoo, using the parent class Attraction
    """
    def __init__(self, name, description):
        super().__init__(name, description)
