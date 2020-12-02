#! /usr/bin/env python3
# coding: utf-8


from models.TableDB import TableDB
from controllers.player_select import *
from controllers.create_player import *
from views.menu_view import *


def players_selection():
    # selection of 8 players
    table_players = TableDB('1', 'known_players')
    list_players = []
    for n in range(8):
        print_menu(f'Select player N° {str(n + 1)}', '\n')
        selected_player = player_select(list_players)
        # creation of a new player
        if selected_player == 'new':
            tournament_player = create_player()
            # save new player
            tournament_player.insert()
            selected_player = table_players.get_last()
        list_players.append(selected_player)
    return list_players
