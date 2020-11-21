from models.builder import Builder


class Round(Builder):  # Definition of class Round
    """Class defining a tour characterized by:
    - its name
    - its start time
    - its end time
    - its list of matches """

    def __init__(self):
        """" Constructor of the class """
        super().__init__()
        self._start = None
        self._end = None
        self._match_list = []

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    @property
    def match_list(self):
        return self._match_list

    @match_list.setter
    def match_list(self, value):
        self._match_list = value
