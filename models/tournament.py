#! /usr/bin/env python3
# coding: utf-8


from models.builder import Builder


class Tournament(Builder):  # Definition of the Tournament class
    """
        Class defining a tournament characterized by:
        - its name
        - its place
        - its date
        - its time controller
        - its number of turns
        - its description
        - its list of players
        - its list of rounds
        - its current step
        - its current turn
        - its current scoreboard
        - its statement
        - its table name on the database
    """

    table_name = 'existing_tournaments'

    def __init__(
            self, name=None, place=None, date=None, mode_game=None, nb_turn=None,
            description=None, current_step=0, current_turn=0, is_ended=0
    ):
        """
            Constructor of the class
            :param name: name of the tournament
            :param place: place of the tournament
            :param date: date of the tournament
            :param mode_game: type of the tournament (blitz/bullet/speed)
            :param nb_turn: number of turn of the tournament
            :param description: description of the tournament
            :param current_step: current step of the tournament execution
            :param current_turn: current turn of the tournament execution
            :param is_ended: statement of the tournament (ended or not)
        """

        super().__init__(name)
        self.place = place
        self.date = date
        self.mode_game = mode_game
        self.nb_turn = nb_turn
        self.description = description
        self.players_index = []
        self.rounds_list = []
        self.scoreboard = {}
        self.current_step = current_step
        self.current_turn = current_turn
        self.is_ended = is_ended

    @staticmethod
    def deserialize(data):
        """
            Serialize the object
            :return: a dictionary
        """
        deserialized = Tournament()
        for attr, value in data.items():
            deserialized.attr = value
        return deserialized
