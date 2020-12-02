#! /usr/bin/env python3
# coding: utf-8


from models.TableDB import *
from views.input_view import *
from views.info_view import *


def turn_results(list_turn, num_turn):
    table_players = TableDB('1', 'known_players')
    score = 0
    match_result = []
    # show the match details
    print_info(f'Match N° {str(num_turn + 1)}: '
               f'playerID {(list_turn[num_turn][0])} '
               f'{table_players.search_by_id(int(list_turn[num_turn][0]))["name"]}'
               f' -VS- playerID {(list_turn[num_turn][1])} '
               f'{table_players.search_by_id(int(list_turn[num_turn][1]))["name"]}', '\n')
    # choose the result
    while score not in ('1', '2', '3'):
        print_info(f'Choose the winner of the match:'
                   f'\nType (1) for ID: {str(list_turn[num_turn][0])}'
                   f', (2) for ID: {str(list_turn[num_turn][1])}'
                   f', (3) for : Draw')
        score = input_data(f' Result: ', '\n')
    if score == '1':
        match_result = [1, 0]
    if score == '2':
        match_result = [0, 1]
    if score == '3':
        match_result = [1 / 2, 1 / 2]
    return match_result
