#! /usr/bin/env python3
# coding: utf-8


def input_data(info, line_break_start='', line_line_break_end=''):
    return input(f'{line_break_start}{info}{line_line_break_end}')


def print_info(info, line_break_start='', line_line_break_end=''):
    print(f'{line_break_start}{info}{line_line_break_end}')


def print_menu(info, line_break_start='', line_line_break_end=''):
    print(f'{line_break_start} --------- {info} --------- {line_line_break_end}')


def print_board(info1, info2, info3='', line_break_start='', line_line_break_end=''):
    print(f'{line_break_start}Player ID {info1} ranked {info2} {info3}{line_line_break_end}')
