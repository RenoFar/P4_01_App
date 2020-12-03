#! /usr/bin/env python3
# coding: utf-8


from models.builder import Builder
from models.tournament import Tournament
from models.player import Player
from views.board_view import BoardView
from views.info_view import InfoView
from views.menu_view import MenuView


class ReportController:

    def __init__(self):
        self.table = Builder()

    def players_sorted(self):
        self.table.name = '1'
        self.table.table_name = 'known_players'
        sorted_ranking = sorted(self.table.all(), key=lambda ranking: ranking['ranking'])
        for sort in range(len(sorted_ranking)):
            BoardView.print_board(
                f'{Player.search_by_rank(sorted_ranking[sort]["ranking"]).doc_id} {sorted_ranking[sort]["name"]} ',
                f'{str(sorted_ranking[sort]["ranking"])}'
            )