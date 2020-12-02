#! /usr/bin/env python3
# coding: utf-8


class InfoView:

    def __init__(self, info, line_break_start, line_line_break_end):
        self.info = info
        self.line_break_start = line_break_start
        self.line_line_break_end = line_line_break_end

    @staticmethod
    def print_info(info, line_break_start='', line_line_break_end=''):
        print(f'{line_break_start}{info}{line_line_break_end}')
