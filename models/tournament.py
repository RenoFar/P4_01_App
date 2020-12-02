#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB
from models.builder import Builder


class Tournament(Builder):  # Definition of the Tournament class
    """Class defining a tournament characterized by:
    - its name
    - its place
    - its place
    - its time controller
    - its number of turns
    - its description
    - its list of rounds
    - its list of players
    - its table_name """

    def __init__(self, name=None, place=None, date=None,
                 mode_game=None, nb_turn=None, description=None, table_name='existing_tournaments'):
        """" Constructor of the class """
        super().__init__(name, table_name)
        self.place = place
        self.date = date
        self.mode_game = mode_game
        self.nb_turn = nb_turn
        self.description = description
        self.players_index = []
        self.rounds_list = []

    def insert(self):
        serialized = {}
        for attr, value in self.__dict__.items():
            if attr != "table_name":
                serialized[attr] = value
        return TinyDB('database.json').table(self.table_name).insert(serialized)
