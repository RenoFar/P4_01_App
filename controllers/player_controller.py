#! /usr/bin/env python3
# coding: utf-8


from models.player import Player
from controllers.builder_controller import BuilderController
from views.info_view import InfoView
from views.menu_view import MenuView
from views.board_view import BoardView


class PlayerController(BuilderController):
    """
        Class grouping together all the player controllers
    """

    def __init__(self, message=None):
        """
            Constructor of the class
        """
        super().__init__(message)

    def players_selection(self):
        """
            Ask for the selection or creation of the 8 tournament players
            :return: a list of them
        """
        # selection of 8 players
        list_chosen_players = []
        for n in range(8):
            MenuView.print_menu(f'Select player N° {str(n + 1)} ')
            selected_player = self.player_select(list_chosen_players)
            if selected_player == 'new':  # create & save a new player
                new_player = self.create_player()
                selected_player = str(
                    Player.insert(new_player.serialize(), Player.table_name)
                )
            list_chosen_players.append(selected_player)
        return list_chosen_players

    def player_select(self, chosen_players):
        """
            Ask for a chosen player among the available
            :param chosen_players: list of the already chosen player
            :return: a string of a player ID or 'new' for create a new one
        """
        # get all known players
        player_db = Player.all(Player.table_name)
        player_choice = '-1'
        while player_choice == '-1':
            # initialize available players
            players_available = []
            InfoView.print_info('List of available players:')
            for a, elt in enumerate(player_db):
                if str(a + 1) not in chosen_players:
                    # exclude players already chosen
                    InfoView.print_info(
                        f'{str(a + 1)}: '
                        f'{elt["name"]} ranking: {elt["ranking"]}'
                    )
                    players_available.append(str(a + 1))

            # choose a player
            self.input_service.message = (
                '\nSelect an available player (1) or add a new player (2): '
            )
            menu_choice = self.input_service.lower_not_in(
                ('1', '2')
            )
            if menu_choice == '1' and len(players_available) > 0:
                # test the available players
                self.input_service.message = (
                    'Select a player number: '
                )
                player_choice = self.input_service.lower_not_in(
                    players_available
                )
            elif menu_choice == '2':
                player_choice = 'new'
        return player_choice

    def create_player(self):
        """
            Ask and format the player information
            :return: a Player Object
        """
        self.input_service.message = (
            'Please enter player name: '
        )
        name = self.input_service.one_char_alphanum()
        self.input_service.message = (
            'Please enter player firstname: '
        )
        firstname = self.input_service.one_char_alphanum()
        self.input_service.message = (
            'Please enter player\'s date of birth in the format d/m/yyyy: '
        )
        birthdate = self.input_service.date_format()
        self.input_service.message = (
            'Please enter the player\'s gender (F / M): '
        )
        gender = self.input_service.lower_not_in(
            ('f', 'm')
        )
        while True:
            self.input_service.message = (
                'Please enter player ranking: '
            )
            ranking = self.input_service.one_char_alphanum()
            try:
                ranking = int(ranking)
                if ranking > 0:
                    # test existing ranking
                    if Player.search_by_rank(ranking) is None:
                        break
                    else:
                        InfoView.print_info(
                            f'\nRank already taken by the player ID :'
                            f'{Player.search_by_rank(ranking).doc_id} '
                            f'name : {Player.search_by_rank(ranking)["name"]}'
                        )
            except ValueError:
                InfoView.print_info('\nPlease enter a positive integer!')
        return Player(name, firstname, birthdate, gender, ranking)

    @staticmethod
    def current_ranking(players_nb, actual_scoreboard, num_turn):
        """
            Give a list of players sorted by ank and score
            :param players_nb: number of the players
            :param actual_scoreboard: actual scoreboard
            :param num_turn: current tournament turn
            :return: a list of players ID in the desired meeting order
        """
        current_ranking = []
        for c in range(len(players_nb)):
            current_ranking.append(
                [players_nb[c],
                 Player.all(Player.table_name)[c]['ranking'],
                 actual_scoreboard[players_nb[c]]
                 ]
            )
        sorted_player_id = []
        if num_turn == 0:
            # sort by rank
            actual_ranking = sorted(current_ranking, key=lambda rank: rank[1])
        else:
            # sort by score then by ranking
            actual_ranking = sorted(current_ranking,
                                    key=lambda k: (-k[2], k[1])
                                    )

        # The best player in the upper half is paired
        # with the best player in the lower half,
        # and so on
        for m in range(len(actual_ranking) // 2):
            player1 = actual_ranking[m][0]
            sorted_player_id.append(player1)
            player2 = actual_ranking[((len(actual_ranking) // 2) + m)][0]
            sorted_player_id.append(player2)
        return sorted_player_id

    def players_score(self, list_turn, num_turn):
        """
            Print the match information and ask for the result
            :param list_turn: list of all the matches of the actual turn
            :param num_turn: actual turn number
            :return: a list of the match results
        """
        match_result = []
        # show the match details
        id_player1 = int(list_turn[num_turn][0])
        id_player2 = int(list_turn[num_turn][1])
        InfoView.print_info(
            f'\nMatch N° {str(num_turn + 1)}: '
            f'playerID {(list_turn[num_turn][0])} '
            f'{Player.search_by_id(id_player1, Player.table_name)["name"]}'
            f' -VS- playerID {(list_turn[num_turn][1])} '
            f'{Player.search_by_id(id_player2, Player.table_name)["name"]}'
        )

        # choose the result
        self.input_service.message = (
            f'Choose the winner of the match: '
            f'\nType (1) for ID: {str(list_turn[num_turn][0])}'
            f', (2) for ID: {str(list_turn[num_turn][1])}, '
            f'(3) for : Draw \n Result: '
        )
        score = self.input_service.lower_not_in(
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
        """
            Show the tournament scoreboard, the players ranking
            then ask and update the new players ranking into the database
            :param board: actual scoreboard
        """
        # show the Tournament scoreboard
        MenuView.print_menu('Tournament scoreboard')
        for num, point in board.items():
            BoardView.print_board(
                num,
                Player.search_by_id(int(num),
                                    Player.table_name)["ranking"],
                f'scores {str(point)}'
            )

        # select the new ranking
        self.new_ranking()

    def new_ranking(self):
        """
            Show the players ranking
            then ask and update the new players ranking into the database
        """
        # show all the players ranking
        MenuView.print_menu('Actual ranking')
        all_players_rank = []
        count = 0
        for elt in Player.all(Player.table_name):
            all_players_rank.append(
                [Player.search_by_rank(int(elt["ranking"])).doc_id,
                 elt["ranking"]]
            )
            InfoView.print_info(f'Player ID {all_players_rank[count][0]} '
                                f'ranking: {all_players_rank[count][1]}'
                                )
            count += 1

        # enter the new ranking
        MenuView.print_menu('Enter the new ranking')
        new_ranking_list = []
        for number in all_players_rank:
            while True:  # control the chosen ranking
                while True:  # control the format
                    self.input_service.message = (
                        f'New ranking of player ID {number[0]} : '
                    )
                    new_ranking = self.input_service.empty_alphanum()
                    try:  # conversion on a positive integer for ranking
                        new_ranking = int(new_ranking)
                        if new_ranking > 0:
                            break
                    except ValueError:
                        InfoView.print_info(
                            '\nPlease enter a positive integer!'
                        )
                if str(new_ranking) not in new_ranking_list:
                    # check for duplicate ranking
                    new_ranking_list.append(str(new_ranking))
                    break
                else:
                    InfoView.print_info(f'\nnew ranking {str(new_ranking)} '
                                        f'already chosen'
                                        )
            # update in the database
            Player.update('ranking',
                          new_ranking,
                          [int(number[0])],
                          Player.table_name
                          )

    @staticmethod
    def players_sorted(key):
        """
            Sort by key the players from the database and print as a list
            :param key: chosen key for the sort
        """
        sorted_players = sorted(Player.all(Player.table_name),
                                key=lambda k: k[key]
                                )
        for sort in range(len(sorted_players)):
            selected = sorted_players[sort]
            BoardView.print_board(
                f'{Player.search_by_rank(selected["ranking"]).doc_id}'
                f' {selected["name"]} ',
                f'{str(selected["ranking"])}'
            )
        return sorted_players

    @staticmethod
    def tournament_players_sorted(key, players_index):
        """
            Sort by the key and print a list of the tournament players
            :param key: chosen key for the sort
            :param players_index: list of the tournament players ID
        """
        list_player_index = []
        for elt in players_index:
            list_player_index.append(
                [elt, Player.search_by_id(int(elt), Player.table_name)['name'],
                 Player.search_by_id(int(elt), Player.table_name)['ranking']]
            )
        sorted_players = sorted(list_player_index, key=lambda k: k[key])
        for sort in range(len(sorted_players)):
            BoardView.print_board(
                f'{sorted_players[sort][0]} {sorted_players[sort][1]} ',
                f'{str(sorted_players[sort][2])}'
            )
