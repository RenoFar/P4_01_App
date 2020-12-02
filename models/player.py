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
                 gender=None, ranking=None):
        """ Constructor of the class """
        super().__init__(name)
        self.firstname = firstname
        self.date_birth = date_birth
        self.gender = gender
        self.ranking = ranking

    def serialize(self):
        serialized = {}
        for attr, value in self.__dict__.items():
            serialized[attr] = value
        return serialized
