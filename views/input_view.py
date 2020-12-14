#! /usr/bin/env python3
# coding: utf-8


class InputView:
    """ Class of the input's view """

    @staticmethod
    def input_data(info):
        """
            Ask an information and return the asked information
            :param info: information to ask
            :return: the asked information
        """
        return input(f'{info}')
