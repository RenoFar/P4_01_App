#! /usr/bin/env python3
# coding: utf-8


from models.player import Player
from services.input_service import InputService
from views.info_view import InfoView
from views.menu_view import MenuView
from views.board_view import BoardView


class PlayerController:

    def __init__(self):
        self.input_service = InputService()

    def players_selection(self):
        # selection of 8 players
        list_chosen_players = []
        for n in range(8):
            MenuView.print_menu(f'Select player N° {str(n + 1)} ')
            selected_player = self.player_select(list_chosen_players)
            if selected_player == 'new':  # creation of a new player
                new_player = self.create_player()
                # save new player
                selected_player = str(Player.insert(new_player.serialize(), Player.table_name))
            list_chosen_players.append(selected_player)
        return list_chosen_players

    def player_select(self, chosen_players):
        # get all known players
        player_db = Player.all(Player.table_name)
        player_choice = '-1'
        while player_choice == '-1':
            # initialize available players
            players_available = []
            MenuView.print_menu('List of available players:')
            for a, elt in enumerate(player_db):
                if str(a + 1) not in chosen_players:  # exclude players already chosen
                    InfoView.print_info(f'{str(a + 1)}: {elt["name"]} ranking: {elt["ranking"]}')
                    players_available.append(str(a + 1))
            # choose a player
            menu_choice = self.input_service.lower_not_in(
                '\nSelect an available player (1) or add a new player (2): ',
                ('1', '2')
            )
            if menu_choice == '1' and len(players_available) > 0:  # test the available players
                player_choice = self.input_service.lower_not_in(
                    'Select a player number: ',
                    players_available
                )
            elif menu_choice == '2':
                player_choice = 'new'
        return player_choice

    def create_player(self):
        name = self.input_service.one_char_alnum('Please enter player name: ')
        firstname = self.input_service.one_char_alnum('Please enter player firstname: ')

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

    @staticmethod
    def current_ranking(players_nb, actual_scoreboard, turn_nb):
        actual_ranking = []
        for c in range(len(players_nb)):
            if turn_nb == 0:  # take the known ranking
                actual_ranking.append([players_nb[c], Player.all(Player.table_name)[c]['ranking']])
            else:  # take the total of the score of the previous rounds
                actual_ranking.append([players_nb[c], actual_scoreboard[players_nb[c]]])
        return actual_ranking

    def players_score(self, list_turn, num_turn):
        score = 0
        match_result = []
        # show the match details
        InfoView.print_info(f'\nMatch N° {str(num_turn + 1)}: '
                            f'playerID {(list_turn[num_turn][0])} '
                            f'{Player.search_by_id(int(list_turn[num_turn][0]), Player.table_name)["name"]}'
                            f' -VS- playerID {(list_turn[num_turn][1])} '
                            f'{Player.search_by_id(int(list_turn[num_turn][1]), Player.table_name)["name"]}')
        # choose the result
        score = self.input_service.lower_not_in(
            f'Choose the winner of the match: \nType (1) for ID: {str(list_turn[num_turn][0])}'
            f', (2) for ID: {str(list_turn[num_turn][1])} (3) for : Draw \n Result: ',
            ('1', '2', '3')
        )
        if score == '1':
            match_result = [1, 0]
        if score == '2':
            match_result = [0, 1]
        if score == '3':
            match_result = [1 / 2, 1 / 2]
        return match_result

    def ranking_update(self, board):
        # show the Tournament scoreboard
        MenuView.print_menu('Tournament scoreboard')
        for num, point in board.items():
            BoardView.print_board(num, Player.search_by_id(int(num), Player.table_name)["ranking"], f'scores {str(point)}')
        # enter the new ranking
        MenuView.print_menu('Enter the new ranking')
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
            Player.update('ranking', new_ranking, [int(number)], Player.table_name)

    @staticmethod
    def players_sorted():
        sorted_ranking = sorted(Player.all(Player.table_name), key=lambda ranking: ranking['ranking'])
        for sort in range(len(sorted_ranking)):
            BoardView.print_board(
                f'{Player.search_by_rank(sorted_ranking[sort]["ranking"]).doc_id} {sorted_ranking[sort]["name"]} ',
                f'{str(sorted_ranking[sort]["ranking"])}'
            )
