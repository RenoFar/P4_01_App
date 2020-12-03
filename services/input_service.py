#! /usr/bin/env python3
# coding: utf-8


from views.input_view import InputView


class InputService:

    @staticmethod
    def one_char_alnum(message):
        element = ''
        while len(element) < 1 or not element.isalnum():
            element = InputView.input_data(message)
        return element

    @staticmethod
    def empty_alnum(message):
        while True:
            element = InputView.input_data(message)
            if element == '' or element.isalnum():
                break
        return element

    @staticmethod
    def date_format(message):
        element = ''
        while len(element) < 1 or not element.isalnum():
            element = InputView.input_data(message)
        return element

    @staticmethod
    def lower_not_in(message, in_check):
        element = ''
        while element.lower() not in in_check:
            element = InputView.input_data(message)
        return element
