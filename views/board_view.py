#! /usr/bin/env python3
# coding: utf-8


class BoardView:

    def __init__(self, player_id, rank, score, line_break_start, line_line_break_end):
        self.player_id = player_id
        self.rank = rank
        self.score = score
        self.line_break_start = line_break_start
        self.line_line_break_end = line_line_break_end

    @staticmethod
    def print_board(player_id, rank, score='', line_break_start='', line_line_break_end=''):
        print(f'{line_break_start}Player ID {player_id} ranked {rank} {score}{line_line_break_end}')
