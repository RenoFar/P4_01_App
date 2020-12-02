#! /usr/bin/env python3
# coding: utf-8


from models.TableDB import *
from views.menu_view import *
from views.input_view import *
from views.info_view import *
from views.board_view import *


def ranking_update(board):
    table_players = TableDB('1', 'known_players')
    update_ranking = ""
    while update_ranking.lower() != 'y':
        update_ranking = InputView.input_data('Do you want to update the ranking? (Y): ', '\n')
    # show the Tournament scoreboard
    MenuView.print_menu('Tournament scoreboard', '\n')
    for num, point in board.items():
        BoardView.print_board(num, table_players.search_by_id(int(num))["ranking"], f'scores {str(point)}')
    # enter the new ranking
    MenuView.print_menu('Enter the new ranking', '\n')
    new_ranking_list = []
    for number in board.keys():
        while True:  # control the chosen ranking
            while True:  # control the format
                new_ranking = InputView.input_data(f'New ranking of player ID {str(number)} : ')
                try:  # conversion on a positive integer for ranking
                    new_ranking = int(new_ranking)
                    if new_ranking > 0:
                        break
                except ValueError:
                    InfoView.print_info('Please enter a positive integer!', '\n')
            if str(new_ranking) not in new_ranking_list:  # check for duplicate ranking
                new_ranking_list.append(str(new_ranking))
                break
            else:
                InfoView.print_info(f'new ranking {str(new_ranking)} already chosen', '\n')
        # update the database
        table_players.update('ranking', new_ranking, [int(number)])
