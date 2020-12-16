#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB, Query


class Builder(object):
    """
        Class defining a builder of the other class characterized by:
        - its name
        - its path to the database
    """

    path = 'database/database.json'

    def __init__(self, name=None):
        """
            Constructor of the class
            :param name: name of the object
        """
        self.name = name

    def serialize(self):
        """
            Serialize the object
            :return: a dictionary
        """
        serialized = {}
        for attr, value in self.__dict__.items():
            serialized[attr] = value
        return serialized

    @classmethod
    def insert(cls, serialized, table_name):
        """
            Insert the serialized object into the TinyDB database
            :param serialized: the dictionary of object to insert
            :param table_name: the table name of the object
            :return: its ID
        """
        return TinyDB(cls.path).table(table_name).insert(serialized)

    @classmethod
    def update(cls, key, value, id_list, table_name):
        """
            update the {key : value} of the database by ID
            :param key: key of the dictionary
            :param value: value of the searched key
            :param id_list: ID of searched object
            :param table_name: table name of the search object
            :return: its ID
        """
        TinyDB(cls.path).table(table_name).update(
            {key: value},
            doc_ids=id_list
        )

    @classmethod
    def all(cls, table_name):
        """
            search all the table chosen in the TinyDB database
            :param table_name: table name of the search objects
            :return: a list of them
        """
        return TinyDB(cls.path).table(table_name).all()

    @classmethod
    def search_by(cls, key, value, table_name):
        """
            Search a specific serialized data by Query method
            :param key: key of the dictionary
            :param value: value of the searched key
            :param table_name: table name of the search object
            :return: a dictionary of it
        """
        return TinyDB(cls.path).table(table_name).get(
            Query()[str(key)] == str(value)
        )

    @classmethod
    def search_by_id(cls, id_number, table_name):
        """
            Search a specific serialized data by its ID
            :param id_number: ID of the search object
            :param table_name: table name of the search object
            :return: a dictionary of it
        """
        return TinyDB(cls.path).table(table_name).get(doc_id=id_number)
