#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB, Query
from models.builder import Builder


class Player(Builder):
    """
        Class defining a player characterized by:
        - its name
        - its firstname
        - its date of birth
        - its gender
        - its ranking
        - its table name on the database
    """

    table_name = 'known_players'

    def __init__(
            self,
            name=None,
            firstname=None,
            date_birth=None,
            gender=None,
            ranking=None
    ):
        """
            Constructor of the class
            :param name: name of the player
            :param firstname: firstname of the player
            :param date_birth: birth date of the player
            :param gender: gender of the player
            :param ranking: rank of the player
        """
        super().__init__(name)
        self.firstname = firstname
        self.date_birth = date_birth
        self.gender = gender
        self.ranking = ranking

    @classmethod
    def search_by_rank(cls, rank):
        """
            Search a specific serialized Player by its rank
            :param rank: rank of the selected object
            :return: a dictionary of it
        """
        return TinyDB(cls.path).table(cls.table_name).get(
            Query()['ranking'] == int(rank)
        )
