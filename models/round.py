from models.builder import Builder


class Round(Builder):  # Definition of class Round
    """Class defining a tour characterized by:
    - its name
    - its start time
    - its end time
    - its list of matches """

    def __init__(self, name=None, start=None, end=None):
        """" Constructor of the class """
        super().__init__(name)
        self.start = start
        self.end = end
        self.match_list = []
