#! /usr/bin/env python3
# coding: utf-8


from controllers.controllers_models import *
from controllers.controllers_db import *
from views.tournament_views import *


def players_selection():
    # selection of 8 players
    list_players = []
    for n in range(8):
        print_menu('Select player number ' + str(n + 1), '\n')
        selected_player = player_select('known_players')

        # creation of a new player
        if selected_player == 'new':
            tournament_player = create_player()
            # save new player
            db_insert('known_players', serialized_player(tournament_player))
            selected_player = db_get('known_players', 'index')

        list_players.append(selected_player)
    return list_players


def player_select(player_list):  # Selection of player
    player_list = db_get(player_list, 'all')
    player_choice = '-1'
    while player_choice == '-1':
        player_listing = []
        print_menu('List of known players:', '\n')
        for a, elt in enumerate(player_list):
            print_info(str(a + 1) + ': ' + str(elt))
            player_listing.append(str(a + 1))
        menu_choice = ""
        while menu_choice not in ('1', '2'):
            menu_choice = input_data('Select a known player (1) or add a new player (2): ', '\n')
            if menu_choice == '1':
                while player_choice not in player_listing:
                    player_choice = input_data('Select a player number: ')
            elif menu_choice == '2':
                player_choice = 'new'
    return player_choice


def current_ranking(players_nb, actual_scoreboard, turn_nb):
    actual_ranking = []
    for c in range(len(players_nb)):
        if turn_nb == 0:  # take the known ranking
            actual_scoreboard[players_nb[c]] = 0
            actual_ranking.append([players_nb[c], db_get('known_players', 'ranking', c)])
        else:  # take the total of the score of the previous rounds
            actual_ranking.append([players_nb[c], actual_scoreboard[players_nb[c]]])
    return actual_ranking


def turn_results(list_turn, num_turn):
    score = 0
    match_result = []
    print_info('Match number ' + str(num_turn + 1) + ' : ' + str(list_turn[num_turn]), '\n')
    while score not in ('1', '2', '3'):
        print_info(f'Choose the winner of the match'
                   f'\n Type 1 for: {str(list_turn[num_turn][0])}'
                   f'\n Type 2 for: {str(list_turn[num_turn][1])}'
                   f'\n Type 3 for: Draw')
        score = input_data(f'\n Your choice: ')
    if score == '1':
        match_result = [1, 0]
    if score == '2':
        match_result = [0, 0]
    if score == '3':
        match_result = [1 / 2, 1 / 2]
    return match_result
