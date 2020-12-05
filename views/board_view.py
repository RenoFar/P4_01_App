#! /usr/bin/env python3
# coding: utf-8


class BoardView:
    """ Class of the board's view """

    @staticmethod
    def print_board(player_id, rank, score=''):
        """ Print the player's board information """
        print(f'Player ID {player_id} ranked {rank} {score}')
