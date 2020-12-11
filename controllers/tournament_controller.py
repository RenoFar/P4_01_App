#! /usr/bin/env python3
# coding: utf-8


from datetime import datetime
from models.tournament import Tournament
from models.round import Round
from controllers.player_controller import PlayerController
from services.input_service import InputService
from views.info_view import InfoView
from views.menu_view import MenuView


class TournamentController:
    """
        Class grouping together all the tournament controllers
    """

    def __init__(self):
        """
            Constructor of the class
        """
        self.tournament = None
        self.turns = None
        self.players = None
        self.input_service = InputService()
        self.tournament_execution()

    def tournament_execution(self):
        """
            Main part of the tournament execution
        """
        # creation of the tournament
        MenuView.print_menu('Tournament creation')
        self.tournament = self.create_tournament()
        # registration in the database
        tournament_id = self.tournament.insert(self.tournament.serialize(), Tournament.table_name)
        MenuView.print_menu('Tournament created')

        # selection of 8 players
        self.input_service.lower_not_in('Do you want to select the players? (Y): ', 'y')
        self.tournament.players_index = PlayerController().players_selection()
        # update the tournament
        Tournament.update('players_index', self.tournament.players_index, [tournament_id], Tournament.table_name)
        MenuView.print_menu(' Tournament players updating ')

        # play the turns
        self.input_service.lower_diff('Do you want to play the turns? (Y): ', 'y')
        turns = self.play_turns()
        # update the tournament
        self.tournament.rounds_list = turns[0].copy()
        Tournament.update('rounds_list', self.tournament.rounds_list, [tournament_id], Tournament.table_name)
        MenuView.print_menu(' Tournament rounds updating ')

        # update the ranking
        self.input_service.lower_diff('\nDo you want to update the ranking? (Y): ', 'y')
        PlayerController().ranking_update(turns[1])
        # show ranking
        MenuView.print_menu('New ranking')
        PlayerController.players_sorted('ranking')

    def create_tournament(self):
        """
            Ask and format the tournament information
            :return: a Tournament Object
        """
        name = self.input_service.one_char_alnum('Please enter the tournament name: ')
        place = self.input_service.one_char_alnum('Please enter the tournament place: ')
        date = self.input_service.date_format('Tournament date in the format m/d/yyyy: ')
        game_mode = self.input_service.lower_not_in(
            'Please enter the tournament mode (bullet / blitz / speed): ',
            ('bullet', 'blitz', 'speed')
        )
        while True:
            nb_turn = self.input_service.empty_alnum(
                'The number of laps by default is 4,\ntype another number or Enter to validate: '
            )
            if len(str(nb_turn)) < 1:  # if nothing is entered
                nb_turn = 4
                break
            else:
                try:
                    nb_turn = int(nb_turn)  # conversion to integer
                    if nb_turn > 0:
                        InfoView.print_info('The number of turns is changed to: ' + str(nb_turn))
                        break
                except ValueError:
                    InfoView.print_info('\nPlease enter a positive integer!')
        description = self.input_service.one_char_alnum('Please enter the tournament description: ')
        return Tournament(name, place, date, game_mode, nb_turn, description)

    def play_turns(self):
        """
            Ask format and determine the Rounds information and the match results
            :return: a list of them
        """
        # initialization of the tournament scoreboard & the list of turns
        scoreboard = {}
        list_turns = []
        for numb in range(len(self.tournament.players_index)):
            scoreboard[self.tournament.players_index[numb]] = 0

        # Play the rounds
        for t in range(self.tournament.nb_turn):
            MenuView.print_menu(f'Execution of round N° {str(t + 1)}')

            # creation of a new round
            turn = self.create_round(t)

            # find the current ranking
            current_classification = PlayerController.current_ranking(self.tournament.players_index, scoreboard, t)

            # generate matches
            list_match = self.create_match(current_classification)

            for m in range(len(list_match)):
                # enter the results of the matches
                match_results = PlayerController().players_score(list_match, m)

                # save the results
                turn.match_list.append(([list_match[m][0], match_results[0]],
                                        [list_match[m][1], match_results[1]]))
                scoreboard[list_match[m][0]] += match_results[0]
                scoreboard[list_match[m][1]] += match_results[1]

            # finish the turn
            self.input_service.lower_diff('\nDo you want to validate the turn? (Y): ', 'y')
            turn.end = datetime.now().strftime("%X")  # local time HH:MM:SS
            list_turns.append([turn.name, turn.start, turn.end, turn.match_list])

        return [list_turns, scoreboard]

    @staticmethod
    def create_round(number_turn):
        """
             format the round information
            :param number_turn: actual turn number
            :return: a Round Object
        """
        name = "round " + str(number_turn + 1)
        start = datetime.now().strftime("%X")  # local time HH:MM:SS
        end = ""
        return Round(name, start, end)

    @staticmethod
    def create_match(selected_players):
        """
            Determine the match configuration
            :param selected_players: list of the players with their ranking
            :return: a list of it
        """
        match_list = []
        ranking_list = sorted(selected_players, key=lambda ranking: ranking[1])
        for index in range(len(ranking_list) // 2):
            player1 = ranking_list[index][0]
            player2 = ranking_list[((len(ranking_list) // 2) + index)][0]
            match_list.append([player1, player2])
        return match_list

    @staticmethod
    def show_tournaments():
        """
            print a list of the actual tournaments from the database
            :return: a list of all tournament ID
        """
        all_tournaments_id = []
        all_tournament = Tournament.all(Tournament.table_name)
        for elt in range(len(all_tournament)):
            InfoView.print_info(
                f'Tournament ID: {all_tournament[elt].doc_id} '
                f'name: {all_tournament[elt]["name"]} '
                f'date: {all_tournament[elt]["date"]} '
                )
            all_tournaments_id.append(str(all_tournament[elt].doc_id))
        return all_tournaments_id

    @staticmethod
    def turns_details(chosen_id):
        """
        Print into a list the rounds details of a chosen tournament
        :param chosen_id:  id of the chosen tournament
        """
        # list of players
        tournament_players = Tournament.search_by_id(int(chosen_id), Tournament.table_name)["players_index"]
        MenuView.print_menu('players in alphabetical order')
        PlayerController.tournament_players_sorted(1, tournament_players)
        MenuView.print_menu('players sorted by ranking')
        PlayerController.tournament_players_sorted(2, tournament_players)

        # details of the rounds
        MenuView.print_menu('Turns details')
        tournament_turns = Tournament.search_by_id(int(chosen_id), Tournament.table_name)["rounds_list"]
        for elt in range(len(tournament_turns)):
            InfoView.print_info(f'\nTournament ID: {chosen_id} Turn N°: {elt + 1} ')
            for elt2 in range(len(tournament_turns[elt])):
                InfoView.print_info(
                    f'match n°: {elt2 + 1} '
                    f'playerID {tournament_turns[elt][3][elt2][0][0]} '
                    f'-VS- playerID {tournament_turns[elt][3][elt2][1][0]} '
                    f': {tournament_turns[elt][3][elt2][0][1]} '
                    f'- {tournament_turns[elt][3][elt2][1][1]}'
                )
