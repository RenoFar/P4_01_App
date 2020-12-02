#! /usr/bin/env python3
# coding: utf-8


from controllers.create_round import *
from controllers.current_ranking import *
from controllers.create_match import *
from controllers.turn_results import *
from views.menu_view import *
from views.input_view import *


def play_turns(new_tournament):
    # initialization of the tournament scoreboard & the list of turns
    scoreboard = {}
    list_turns = []
    for numb in range(len(new_tournament.players_index)):
        scoreboard[new_tournament.players_index[numb]] = 0
    # Play the rounds
    for t in range(new_tournament.nb_turn):
        print_menu(f'Execution of round N° {str(t + 1)}', '\n')
        # creation of a new round
        turn = create_round(t)
        # find the current ranking
        current_classification = current_ranking(new_tournament.players_index, scoreboard, t)
        # generate matches
        list_match = create_match(current_classification)
        # enter the results of the matches
        for m in range(len(list_match)):
            match_results = turn_results(list_match, m)
            # save the results
            turn.match_list.append(([list_match[m][0], match_results[0]], [list_match[m][1], match_results[1]]))
            scoreboard[list_match[m][0]] += match_results[0]
            scoreboard[list_match[m][1]] += match_results[1]
        # finish the turn
        next_turn = ""
        while next_turn.lower() != 'y':
            next_turn = input_data('Do you want to validate the turn? (Y): ', '\n')
        turn.end = "end"
        list_turns.append(turn)
    return [list_turns, scoreboard]
