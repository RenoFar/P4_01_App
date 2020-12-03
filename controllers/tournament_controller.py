#! /usr/bin/env python3
# coding: utf-8


from models.builder import Builder
from models.tournament import Tournament
from models.round import Round
from controllers.player_controller import PlayerController
from controllers.report_controller import ReportController
from services.input_service import InputService
from views.info_view import InfoView
from views.menu_view import MenuView


class TournamentController:

    def __init__(self):
        self.tournament = None
        self.turns = None
        self.players = None
        self.input_service = InputService()
        self.table_db = Builder("tournament", "existing_tournaments")
        self.tournament_execution()

    def tournament_execution(self):
        # creation of the tournament
        self.tournament = self.create_tournament()
        # registration in the database
        tournament_id = self.table_db.insert(self.tournament.serialize())
        MenuView.print_menu('Tournament created')
        # selection of 8 players
        self.tournament.players_index = PlayerController().players_selection()
        # update the tournament
        self.table_db.update('players_index', self.tournament.players_index, [tournament_id])
        MenuView.print_menu('\n Tournament players updating \n')
        # play the turns
        turns = self.play_turns()
        # update the tournament
        self.tournament.rounds_list = turns[0].copy()
        self.table_db.update('rounds_list', self.tournament.rounds_list, [tournament_id])
        MenuView.print_menu('\n Tournament rounds updating \n')
        # update the ranking
        self.input_service.lower_not_in('Do you want to update the ranking? (Y): ', 'y')
        PlayerController().ranking_update(turns[1])
        # show ranking
        MenuView.print_menu('\nNew ranking')
        ReportController().players_sorted()

    def create_tournament(self):
        name = self.input_service.one_char_alnum('Please enter the tournament name: ')
        place = self.input_service.one_char_alnum('Please enter the tournament place: ')

        # TODO
        date = self.input_service.date_format('Tournament date: ')

        game_mode = self.input_service.lower_not_in(
            'Please enter the tournament mode (bullet / blitz / speed): ',
            ('bullet', 'blitz', 'speed')
        )
        while True:
            nb_turn = self.input_service.empty_alnum(
                'The number of laps by default is 4,\n type another number or Enter to validate: '
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
        # initialization of the tournament scoreboard & the list of turns
        scoreboard = {}
        list_turns = []
        for numb in range(len(self.tournament.players_index)):
            scoreboard[self.tournament.players_index[numb]] = 0
        # Play the rounds
        for t in range(self.tournament.nb_turn):
            MenuView.print_menu(f'\nExecution of round N° {str(t + 1)}')
            # creation of a new round
            turn = self.create_round(t)
            # find the current ranking
            current_classification = self.current_ranking(self.tournament.players_index, scoreboard, t)
            # generate matches
            list_match = self.create_match(current_classification)
            # enter the results of the matches
            for m in range(len(list_match)):
                match_results = self.turn_results(list_match, m)
                # save the results
                turn.match_list.append(([list_match[m][0], match_results[0]], [list_match[m][1], match_results[1]]))
                scoreboard[list_match[m][0]] += match_results[0]
                scoreboard[list_match[m][1]] += match_results[1]
            # finish the turn
            self.input_service.lower_not_in('\nDo you want to validate the turn? (Y): ', 'y')
            turn.end = "end"
            list_turns.append([turn.name, turn.start, turn.end, turn.match_list])
        return [list_turns, scoreboard]

    @staticmethod
    def create_round(number_turn):
        name = "round " + str(number_turn + 1)
        start = "start"
        end = ""
        return Round(name, start, end)

    def current_ranking(self, players_nb, actual_scoreboard, turn_nb):
        actual_ranking = []
        for c in range(len(players_nb)):
            if turn_nb == 0:  # take the known ranking
                actual_ranking.append([players_nb[c], self.table_db.all()[c]['ranking']])
            else:  # take the total of the score of the previous rounds
                actual_ranking.append([players_nb[c], actual_scoreboard[players_nb[c]]])
        return actual_ranking

    @staticmethod
    def create_match(selected_players):
        match_list = []
        ranking_list = sorted(selected_players, key=lambda ranking: ranking[1])
        for index in range(len(ranking_list) // 2):
            player1 = ranking_list[index][0]
            player2 = ranking_list[((len(ranking_list) // 2) + index)][0]
            match_list.append([player1, player2])
        return match_list

    def turn_results(self, list_turn, num_turn):
        score = 0
        match_result = []
        # show the match details
        InfoView.print_info(f'\nMatch N° {str(num_turn + 1)}: '
                            f'playerID {(list_turn[num_turn][0])} '
                            f'{self.table_db.search_by_id(int(list_turn[num_turn][0]))["name"]}'
                            f' -VS- playerID {(list_turn[num_turn][1])} '
                            f'{self.table_db.search_by_id(int(list_turn[num_turn][1]))["name"]}')
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
