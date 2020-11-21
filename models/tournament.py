from models.builder import Builder


class Tournament(Builder):  # Definition of the Tournament class
    """Class defining a tournament characterized by:
    - its name
    - its place
    - its place
    - its number of turns
    - its list of rounds
    - its list of players
    - its time controller
    - its description """

    def __init__(self):
        """" Constructor of the class """
        super().__init__()
        self._place = None
        self._date = None
        self._nb_turn = None
        self._mode_game = None
        self._description = None
        self._rounds_list = []
        self._players_index = []

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        self._place = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def nb_turn(self):
        return self._nb_turn

    @nb_turn.setter
    def nb_turn(self, value):
        self._nb_turn = value

    @property
    def mode_game(self):
        return self._mode_game

    @mode_game.setter
    def mode_game(self, value):
        self._mode_game = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def rounds_list(self):
        return self._rounds_list

    @rounds_list.setter
    def rounds_list(self, value):
        self._rounds_list = value

    @property
    def players_index(self):
        return self._players_index

    @players_index.setter
    def players_index(self, value):
        self._players_index = value
