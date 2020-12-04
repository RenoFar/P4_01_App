#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB, Query


class Builder(object):
    """Class Builder"""

    path = 'database/database.json'

    def __init__(self, name=None):
        """" Constructor of the class """
        self.name = name

    def serialize(self):
        serialized = {}
        for attr, value in self.__dict__.items():
            serialized[attr] = value
        return serialized

    @classmethod
    def insert(cls, serialized, table_name):
        return TinyDB(cls.path).table(table_name).insert(serialized)

    @classmethod
    def update(cls, key, value, id_list, table_name):
        TinyDB(cls.path).table(table_name).update({key: value}, doc_ids=id_list)

    @classmethod
    def all(cls, table_name):
        return TinyDB(cls.path).table(table_name).all()

    @classmethod
    def search_by(cls, key, value, table_name):
        return TinyDB(cls.path).table(table_name).get(Query()[str(key)] == str(value))

    @classmethod
    def search_by_id(cls, id_number, table_name):
        return TinyDB(cls.path).table(table_name).get(doc_id=id_number)

"""    @classmethod
    def get_last(cls):
        table = TinyDB(cls.path).table(cls.table_name)
        return str(table.all()[len(table) - 1].doc_id)
"""