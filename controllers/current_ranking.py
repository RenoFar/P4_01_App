#! /usr/bin/env python3
# coding: utf-8


from models.TableDB import *


def current_ranking(players_nb, actual_scoreboard, turn_nb):
    table_players = TableDB('1', 'known_players')
    actual_ranking = []
    for c in range(len(players_nb)):
        if turn_nb == 0:  # take the known ranking
            actual_ranking.append([players_nb[c], table_players.all()[c]['ranking']])
        else:  # take the total of the score of the previous rounds
            actual_ranking.append([players_nb[c], actual_scoreboard[players_nb[c]]])
    return actual_ranking
