#! /usr/bin/env python3
# coding: utf-8


from models.TableDB import *
from views.board_view import *


def players_sorted():
    table_players = TableDB('1', 'known_players')
    sorted_ranking = sorted(table_players.all(), key=lambda ranking: ranking['ranking'])
    for sort in range(len(sorted_ranking)):
        print_board(f'{table_players.search_by_rank(sorted_ranking[sort]["ranking"]).doc_id} '
                    f'{sorted_ranking[sort]["name"]} ',
                    f'{str(sorted_ranking[sort]["ranking"])}')
