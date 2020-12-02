#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB
from models.builder import Builder


class Player(Builder):  # Definition of the Player class
    """Class defining a player characterized by:
    - its name
    - its firstname
    - its date of birth
    - its gender
    - its ranking
    - its table_name"""

    def __init__(self, name=None, firstname=None, date_birth=None,
                 gender=None, ranking=None, table_name='known_players'):
        """ Constructor of the class """
        super().__init__(name, table_name)
        self.firstname = firstname
        self.date_birth = date_birth
        self.gender = gender
        self.ranking = ranking

    def insert(self):
        serialized = {}
        for attr, value in self.__dict__.items():
            if attr != "table_name":
                serialized[attr] = value
        return TinyDB('database.json').table(self.table_name).insert(serialized)
