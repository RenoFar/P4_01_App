#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB, Query
from models.builder import Builder


class TableDB(Builder):
    """Class TableDB"""

    def __init__(self, name=None, table_name=None):
        """" Constructor of the class """
        super().__init__(name, table_name)

    def update(self, key, value, id_list):
        TinyDB('database.json').table(self.table_name).update({key: value}, doc_ids=id_list)

    def all(self):
        return TinyDB('database.json').table(self.table_name).all()

    def get_last(self):
        table = TinyDB('database.json').table(self.table_name)
        return str(table.all()[len(table) - 1].doc_id)

    def search_by(self, key, value):
        return TinyDB('database.json').table(self.table_name).get(Query()[str(key)] == str(value))

    def search_by_rank(self, rank):
        return TinyDB('database.json').table(self.table_name).get(Query()['ranking'] == int(rank))
