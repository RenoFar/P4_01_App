#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB


class Builder(object):
    """Class Builder"""

    def __init__(self, name=None):
        """" Constructor of the class """
        self.name = name
