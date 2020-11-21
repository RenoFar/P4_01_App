from models.builder import Builder


class Player(Builder):  # Definition of the Player class
    """Class defining a player characterized by:
    - its name
    - its firstname
    - its date of birth
    - its gender
    - its ranking """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self._firstname = None
        self._date_birth = None
        self._gender = None
        self._index = None
        self._ranking = None

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value

    @property
    def date_birth(self):
        return self._date_birth

    @date_birth.setter
    def date_birth(self, value):
        self._date_birth = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def ranking(self, value):
        self._ranking = value
