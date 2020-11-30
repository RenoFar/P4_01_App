#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB


class Builder:
    """Class Builder"""

    def __init__(self, name=None, table_name=None):
        """" Constructor of the class """
        self.name = name
        self.table_name = table_name

    def update(self, key, value, id_list):
        TinyDB('database.json').table(self.table_name).update({key: value}, doc_ids= id_list)

    def insert(self, data_dict):
        TinyDB('database.json').table(self.table_name).insert(data_dict)

    def all(self):
        return TinyDB('database.json').table(self.table_name).all()

    def get_last(self):
        table = TinyDB('database.json').table(self.table_name)
        return str(table.all()[len(table) - 1].doc_id)

     def serialize(self):
        serialized = {}
        for attr, value in self.__dict__.items():
            if attr != "table_name":
                serialized[attr] = value
        return serialized
