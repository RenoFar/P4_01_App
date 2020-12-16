#! /usr/bin/env python3
# coding: utf-8


from services.input_service import InputService


class BuilderController(object):
    """
        Class defining a builder of the other class characterized by:
        - its input service
    """

    def __init__(self, message=None):
        """
            Constructor of the class
            :param message: information to ask
        """
        self.input_service = InputService(message)
