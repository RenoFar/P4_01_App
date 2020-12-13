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

    def tournament_execution(self, t_id=0, step=0, turn=0):
        """
            Tournament processing step by step
            :param t_id: id of the chosen tournament
            :param step: current step of the chosen tournament
            :param turn: current turn of the chosen tournament
        """
        if step == 0:
            # creation of the tournament
            self.tournament_step_zero()
        if step == 1:
            # selection of 8 players
            self.tournament_step_one(t_id)
        if step == 2:
            # play the turns
            self.tournament_step_two(t_id, turn)
        if step == 3:
            # update the ranking
            self.tournament_step_three(t_id)
            MenuView.print_menu(' Tournament ended ')

    def tournament_step_zero(self):
        # creation of the tournament
        MenuView.print_menu('Tournament creation')
        self.tournament = self.create_tournament()
        # registration in the database
        t_id = self.tournament.insert(self.tournament.serialize(), Tournament.table_name)
        Tournament.update('current_step', 1, [t_id], Tournament.table_name)
        MenuView.print_menu('Tournament created')
        choice0 = self.input_service.lower_not_in(
            'Do you want to select the players (y/n): ',
            ('y', 'n')
        )
        if choice0 == 'y':
            self.tournament_execution(t_id, 1)

    def tournament_step_one(self, t_id):
        # selection of 8 players
        self.tournament = Tournament(**Tournament.search_by_id(t_id, Tournament.table_name))
        self.tournament.players_index = PlayerController().players_selection()
        # update the tournament
        Tournament.update('players_index', self.tournament.players_index, [t_id], Tournament.table_name)
        Tournament.update('current_step', 2, [t_id], Tournament.table_name)
        MenuView.print_menu(' Tournament players saved ')
        choice1 = self.input_service.lower_not_in(
            'Do you want to play the turns (y/n): ',
            ('y', 'n')
        )
        if choice1 == 'y':
            self.tournament_execution(t_id, 2)

    def tournament_step_two(self, t_id, turn_num):
        self.tournament = Tournament(**Tournament.search_by_id(t_id, Tournament.table_name))

        # initialize the scoreboard
        if turn_num == 0:
            for numb in range(len(self.tournament.players_index)):
                self.tournament.scoreboard[self.tournament.players_index[numb]] = 0

        # play the turns
        actual_turn = self.play_turns(self.tournament, t_id, turn_num)

        if actual_turn == 3:
            # finish the turns
            Tournament.update('current_step', 3, [t_id], Tournament.table_name)
            MenuView.print_menu(' Tournament rounds saved ')
            choice2 = self.input_service.lower_not_in(
                'Do you want to update the ranking (y/n): ',
                ('y', 'n')
            )
            if choice2 == 'y':
                self.tournament_execution(t_id, 3)

    def tournament_step_three(self, t_id):
        # update the ranking
        self.tournament = Tournament(**Tournament.search_by_id(t_id, Tournament.table_name))
        PlayerController().ranking_update(self.tournament.scoreboard)
        # show ranking
        MenuView.print_menu('New ranking')
        PlayerController.players_sorted('ranking')
        Tournament.update('current_step', 4, [t_id], Tournament.table_name)
        Tournament.update('is_ended', 1, [t_id], Tournament.table_name)

    def choose_tournament(self):
        """
            Show all the not ended tournament and ask to choose one
            :return: the not ended tournament chosen or None
        """
        # show tournament not ended
        MenuView.print_menu('Unfinished tournaments')
        not_ended = self.show_tournaments([0])
        if len(not_ended) < 1:
            return None
        else:
            # ask for choice
            not_ended_id = self.input_service.lower_not_in(
                'Please select an ID: ',
                not_ended
            )
            return Tournament.search_by_id(int(not_ended_id), Tournament.table_name)

    def create_tournament(self):
        """
            Ask and format the tournament information
            :return: a Tournament Object
        """
        players_index = []
        rounds_list = []
        scoreboard = {}
        name = self.input_service.one_char_alnum('Please enter the tournament name: ')
        place = self.input_service.one_char_alnum('Please enter the tournament place: ')
        date = self.input_service.date_format('Please enter the tournament date: ')
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
        return Tournament(name, place, date, game_mode, nb_turn, description, players_index, rounds_list, scoreboard)

    def play_turns(self, tournament, t_id, turn_num):
        # play the turns
        turn_left = tournament.nb_turn - turn_num
        current_turn = turn_num
        for t in range(turn_left):
            current_turn += t
            MenuView.print_menu(f'Execution of round N° {str(current_turn + 1)}')

            # creation of a new round
            self.input_service.lower_diff('\nDo you want to start the turn? (y): ', 'y')
            turn = self.create_round(current_turn)

            # find the current ranking
            current_classification = PlayerController.current_ranking(
                tournament.players_index,
                tournament.scoreboard,
                t
            )

            # generate matches
            list_match = self.create_match(current_classification)
            InfoView.print_info(f'Turn start at {turn.start} : Matches in progress...')

            # enter the results of the matches
            self.input_service.lower_diff('\nDo you want to enter the results? (y): ', 'y')
            for m in range(len(list_match)):
                match_results = PlayerController().players_score(list_match, m)

                # save the results
                turn.match_list.append(([list_match[m][0], match_results[0]],
                                        [list_match[m][1], match_results[1]]))
                self.tournament.scoreboard[list_match[m][0]] += match_results[0]
                self.tournament.scoreboard[list_match[m][1]] += match_results[1]

            # finish the turn
            self.input_service.lower_diff('\nDo you want to end the turn? (y): ', 'y')
            turn.end = datetime.now().strftime("%X")  # local time HH:MM:SS
            self.tournament.rounds_list += [[turn.name, turn.start, turn.end, turn.match_list]]
            # update the tournament
            Tournament.update('rounds_list', self.tournament.rounds_list, [t_id], Tournament.table_name)
            Tournament.update('scoreboard', self.tournament.scoreboard, [t_id], Tournament.table_name)
            Tournament.update('current_turn', current_turn + 1, [t_id], Tournament.table_name)
            MenuView.print_menu(f' Turn n° {current_turn + 1} saved ')
            if current_turn == 3:
                break
            else:
                choice4 = self.input_service.lower_not_in(
                    'Do you want to play the next turn (y/n): ',
                    ('y', 'n')
                )
                if choice4 == 'n':
                    break
        return current_turn

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
    def show_tournaments(statement):
        """
            print a list of the actual tournaments from the database
            :param statement: statement of the tournament chosen (ended or not)
            :return: a list of all tournament ID
        """
        all_tournaments_id = []
        all_tournament = Tournament.all(Tournament.table_name)
        for elt in range(len(all_tournament)):
            if all_tournament[elt]["is_ended"] in statement:
                if all_tournament[elt]["is_ended"] == 0:
                    status = " - NOT FINISHED"
                else:
                    status = ""
                InfoView.print_info(
                    f'Tournament ID: {all_tournament[elt].doc_id} '
                    f'name: {all_tournament[elt]["name"]} '
                    f'date: {all_tournament[elt]["date"]} '
                    f'{status}'
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
