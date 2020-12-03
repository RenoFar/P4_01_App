#! /usr/bin/env python3
# coding: utf-8


class BoardView:

    @staticmethod
    def print_board(player_id, rank, score=''):
        print(f'Player ID {player_id} ranked {rank} {score}')
