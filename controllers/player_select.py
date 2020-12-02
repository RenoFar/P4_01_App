#! /usr/bin/env python3
# coding: utf-8


from models.TableDB import TableDB
from views.menu_view import *
from views.info_view import *
from views.input_view import *


def player_select(chosen_players):
    # get all known players
    table_players = TableDB('1', 'known_players')
    player_list = table_players.all()
    player_choice = '-1'
    while player_choice == '-1':
        # initialize available players
        player_listing = []
        print_menu('List of available players:')
        for a, elt in enumerate(player_list):
            if str(a + 1) not in chosen_players:  # exclude players already chosen
                print_info(f'{str(a + 1)}: {elt["name"]} ranking: {elt["ranking"]}')
                player_listing.append(str(a + 1))
        # choose a player
        menu_choice = ""
        while menu_choice not in ('1', '2'):
            menu_choice = input_data('Select an available player (1) or add a new player (2): ', '\n')
            if menu_choice == '1' and len(player_listing) > 0:
                while player_choice not in player_listing:  # test the available players
                    player_choice = input_data('Select a player number: ')
            elif menu_choice == '2':
                player_choice = 'new'
    return player_choice
