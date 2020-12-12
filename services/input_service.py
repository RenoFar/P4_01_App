#! /usr/bin/env python3
# coding: utf-8


from datetime import datetime
from views.input_view import InputView
from views.info_view import InfoView


class InputService:
    """ Class grouping together all the Input services """

    @staticmethod
    def one_char_alnum(message):
        """
            Ask for an information
            :param message: asking information message
            :return: an input element with one character at least and alphanumeric
        """
        element = ''
        while len(element) < 1 or not element.isalnum():
            element = InputView.input_data(message)
        return element

    @staticmethod
    def empty_alnum(message):
        """
            Ask for an information
            :param message: asking information message
            :return: an input element empty or alphanumeric
        """
        while True:
            element = InputView.input_data(message)
            if element == '' or element.isalnum():
                break
        return element

    @staticmethod
    def date_format(message):
        """
            Ask for a date information and test the format
            :param message: asking information message
            :return: an input element with the datetime format: '%d/%m/%Y'
        """
        while True:
            try:
                element = datetime.strptime(InputView.input_data(message), '%d/%m/%Y')
                break
            except ValueError:
                InfoView.print_info('\nPlease enter a date in the format d/m/yyyy')
        return element.strftime('%d/%m/%Y')

    @staticmethod
    def lower_not_in(message, in_check):
        """
            Ask for an information
            :param message: asking information message
            :param in_check: container of the possible inputs
            :return: an input element contained in in_check
        """
        element = ''
        while element.lower() not in in_check:
            element = InputView.input_data(message)
        return element

    @staticmethod
    def lower_diff(message, in_check):
        """
            Ask for an information
            :param message: asking information message
            :param in_check: the excepted input
            :return: the excepted input
        """
        element = ''
        while element.lower() != in_check:
            element = InputView.input_data(message)
        return element
