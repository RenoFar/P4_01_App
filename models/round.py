#! /usr/bin/env python3
# coding: utf-8


class Round:
    """
        Class defining a tour characterized by:
        - its name
        - its start time
        - its end time
        - its list of matches
    """

    def __init__(self, name=None, start=None, end=None):
        """
            Constructor of the class
            :param name: name of the turn
            :param start: start time of the turn
            :param end: end time of the turn
        """
        self.name = name
        self.start = start
        self.end = end
        self.match_list = []
