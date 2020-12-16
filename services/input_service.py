#! /usr/bin/env python3
# coding: utf-8


from datetime import datetime
from views.input_view import InputView
from views.info_view import InfoView


class InputService:
    """
        Class containing together all the Input services
    """

    def __init__(self, message=None):
        self.message = message

    def one_char_alphanum(self):
        """
            Ask for an information
            :return: an alphanumeric input with one character at least
        """
        element = ''
        while len(element) < 1 or not element.isalnum():
            element = InputView.input_data(self.message)
        return element

    def empty_alphanum(self):
        """
            Ask for an information
            :return: an input element empty or alphanumeric
        """
        while True:
            element = InputView.input_data(self.message)
            if element == '' or element.isalnum():
                break
        return element

    def date_format(self):
        """
            Ask for a date information and test the format
            :return: an input element with the datetime format: '%d/%m/%Y'
        """
        while True:
            try:
                element = datetime.strptime(
                    InputView.input_data(self.message),
                    '%d/%m/%Y'
                )
                break
            except ValueError:
                InfoView.print_info(
                    '\nPlease enter a date in the format d/m/yyyy'
                )
        return element.strftime('%d/%m/%Y')

    def lower_not_in(self, in_check):
        """
            Ask for an information
            :param in_check: container of the possible inputs
            :return: an input element contained in in_check
        """
        element = ''
        while element.lower() not in in_check:
            element = InputView.input_data(self.message)
        return element

    def lower_diff(self, in_check):
        """
            Ask for an information
            :param in_check: the excepted input
            :return: the excepted input
        """
        element = ''
        while element.lower() != in_check:
            element = InputView.input_data(self.message)
        return element
