#! /usr/bin/env python3
# coding: utf-8


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

    def __init__(self, name=None, place=None, date=None, nb_turn=None, mode_game=None, description=None):
        """" Constructor of the class """
        super().__init__(name)
        self.place = place
        self.date = date
        self.nb_turn = nb_turn
        self.mode_game = mode_game
        self.description = description
        self.rounds_list = []
        self.players_index = []
