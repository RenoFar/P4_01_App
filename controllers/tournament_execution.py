#! /usr/bin/env python3
# coding: utf-8


from controllers.players_selection import *
from controllers.create_tournament import *
from controllers.play_turns import *
from controllers.ranking_update import *
from controllers.players_sorted import *
from views.menu_view import *


def tournament_execution():
    # creation of the tournament
    new_tournament = create_tournament()
    # registration in the database
    new_tournament.insert()
    print_menu('Tournament created', '\n')
    # selection of 8 players
    new_tournament.players_index = players_selection()
    # update the tournament
    table_tournaments = TableDB('2', 'existing_tournaments')
    table_tournaments.update('players_index', new_tournament.players_index, [int(table_tournaments.get_last())])
    print_menu('Tournament players updating', '\n', '\n')
    # play the turns
    turns = play_turns(new_tournament)
    # update the tournament
    new_tournament.rounds_list.append(turns[0])
    table_tournaments.update('rounds_list', new_tournament.rounds_list, [int(table_tournaments.get_last())])
    print_menu('Tournament rounds updating', '\n', '\n')
    # update the ranking
    ranking_update(turns[1])
    # show ranking
    print_menu('New ranking', '\n')
    players_sorted()
















