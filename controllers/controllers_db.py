#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB
from views.tournament_views import *


def initialize_db():
    TinyDB('../models/database.json')


def serialized_player(player):
    return {'name': player.name, 'firstname': player.firstname, 'date_birth': player.date_birth,
            'gender': player.gender, 'ranking': player.ranking}


def serialized_tournament(tournament):
    return {'name': tournament.name, 'place': tournament.place, 'date': tournament.date,
            'mode_game': tournament.mode_game, 'nb_turn': tournament.nb_turn,
            'description': tournament.description, 'players_index': tournament.players_index,
            'rounds_list': tournament.rounds_list}


def db_insert(table, data_dict):
    TinyDB('database.json').table(table).insert(data_dict)


def db_update(table, key, value, data_id_list):
    TinyDB('database.json').table(table).update({key: value}, doc_ids=data_id_list)


def db_get(table_name, info, nb=None):
    table = TinyDB('database.json').table(table_name)
    if info == 'index':
        result = str(table.all()[len(table) - 1].doc_id)
    elif info == 'all':
        result = table.all()
    else:
        result = table.all()[nb][info]
    return result


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
