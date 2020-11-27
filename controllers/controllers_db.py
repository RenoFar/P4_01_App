#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB, Query


def initialize_db():
    TinyDB('database.json')


def db_insert(table, data_dict):
    TinyDB('database.json').table(table).insert(data_dict)


def db_update(table, key, value, id_list):
    TinyDB('database.json').table(table).update({key: value}, doc_ids= id_list)


def db_get(table_name, info, nb=None):
    table = TinyDB('database.json').table(table_name)
    if info == 'index':
        result = str(table.all()[len(table) - 1].doc_id)
    elif info == 'all':
        result = table.all()
    else:
        result = table.all()[nb][info]
    return result


def db_search_id(rank):
    players_id = TinyDB('database.json').table('known_players').get(Query()['ranking'] == rank).doc_id
    return players_id


def serialized_player(player):
    return {'name': player.name, 'firstname': player.firstname, 'date_birth': player.date_birth,
            'gender': player.gender, 'ranking': player.ranking}


def serialized_tournament(tournament):
    return {'name': tournament.name, 'place': tournament.place, 'date': tournament.date,
            'mode_game': tournament.mode_game, 'nb_turn': tournament.nb_turn,
            'description': tournament.description, 'players_index': tournament.players_index,
            'rounds_list': tournament.rounds_list}
