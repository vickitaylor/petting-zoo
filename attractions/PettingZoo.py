from .attraction import Attraction

class PettingZoo(Attraction):
    """class to create the petting zoo
    """
    def __init__(self, name, description):
        super().__init__(name, description)
