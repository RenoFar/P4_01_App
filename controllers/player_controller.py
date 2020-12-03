#! /usr/bin/env python3
# coding: utf-8


from models.player import Player
from models.builder import Builder
from services.input_service import InputService
from views.info_view import InfoView
from views.menu_view import MenuView
from views.board_view import BoardView


class PlayerController:

    def __init__(self):
        self.input_service = InputService()
        self.table_db = Builder('1', 'known_players')

    def players_selection(self):
        # selection of 8 players
        list_players = []
        for n in range(8):
            MenuView.print_menu(f'\nSelect player N° {str(n + 1)} ')
            selected_player = self.player_select(list_players)
            if selected_player == 'new':  # creation of a new player
                tournament_player = self.create_player()
                # save new player
                tournament_player.insert()
                selected_player = self.table_db.get_last()
            list_players.append(selected_player)
        return list_players

    def player_select(self, chosen_players):
        # get all known players
        player_list = self.table_db.all()
        player_choice = '-1'
        while player_choice == '-1':
            # initialize available players
            player_listing = []
            MenuView.print_menu('List of available players:')
            for a, elt in enumerate(player_list):
                if str(a + 1) not in chosen_players:  # exclude players already chosen
                    InfoView.print_info(f'{str(a + 1)}: {elt["name"]} ranking: {elt["ranking"]}')
                    player_listing.append(str(a + 1))
            # choose a player
            menu_choice = self.input_service.lower_not_in(
                '\nSelect an available player (1) or add a new player (2): ',
                ('1', '2')
            )
            if menu_choice == '1' and len(player_listing) > 0:  # test the available players
                player_choice = self.input_service.lower_not_in(
                    'Select a player number: ',
                    player_listing
                )
            elif menu_choice == '2':
                player_choice = 'new'
        return player_choice

    def create_player(self):
        name = self.input_service.one_char_alnum('Please enter player name: ')
        firstname = self.input_service.one_char_alnum('Please enter player name: ')

        # TODO
        birthdate = self.input_service.date_format('Please enter player\'s date of birth: ')

        gender = self.input_service.lower_not_in(
            'Please enter the player\'s gender (F / M): ',
            ('f', 'm')
        )
        while True:
            ranking = self.input_service.one_char_alnum('Please enter player ranking: ')
            try:
                ranking = int(ranking)
                if ranking > 0:
                    break
            except ValueError:
                InfoView.print_info('\nPlease enter a positive integer!')
        return Player(name, firstname, birthdate, gender, ranking)

    def ranking_update(self, board):
        # show the Tournament scoreboard
        MenuView.print_menu('\nTournament scoreboard')
        for num, point in board.items():
            BoardView.print_board(num, self.table_db.search_by_id(int(num))["ranking"], f'scores {str(point)}')
        # enter the new ranking
        MenuView.print_menu('\nEnter the new ranking')
        new_ranking_list = []
        for number in board.keys():
            while True:  # control the chosen ranking
                while True:  # control the format
                    new_ranking = self.input_service.empty_alnum(f'New ranking of player ID {str(number)} : ')
                    try:  # conversion on a positive integer for ranking
                        new_ranking = int(new_ranking)
                        if new_ranking > 0:
                            break
                    except ValueError:
                        InfoView.print_info('\nPlease enter a positive integer!')
                if str(new_ranking) not in new_ranking_list:  # check for duplicate ranking
                    new_ranking_list.append(str(new_ranking))
                    break
                else:
                    InfoView.print_info(f'\nnew ranking {str(new_ranking)} already chosen')
            # update the database
            self.table_db.update('ranking', new_ranking, [int(number)])
