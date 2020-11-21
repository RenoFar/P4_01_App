class Builder:
    """Class Builder"""

    def __init__(self):
        """" Constructor of the class """
        self.__name = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
