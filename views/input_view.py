#! /usr/bin/env python3
# coding: utf-8


class InputView:

    def __init__(self, info, line_break_start, line_line_break_end):
        self.info = info
        self.line_break_start = line_break_start
        self.line_line_break_end = line_line_break_end

    @staticmethod
    def input_data(info, line_break_start='', line_line_break_end=''):
        return input(f'{line_break_start}{info}{line_line_break_end}')


