#! /usr/bin/env python3
# coding: utf-8


class InputView:
    """ Class of the input's view """

    @staticmethod
    def input_data(info):
        """ Ask and return the general information """
        return input(f'{info}')
