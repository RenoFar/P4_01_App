#! /usr/bin/env python3
# coding: utf-8


from controllers.controllers_models import *
from controllers.controllers_db import *
from views.tournament_views import *


def tournament_execution():
    # initialization of variables
    initialize_db()

    # creation of the tournament
    new_tournament = create_tournament()
    """db_insert('existing_tournaments', serialized_tournament(new_tournament))"""

    # selection of 8 players
    new_tournament.players_index = players_selection()

    # initialization of the tournament scoreboard
    scoreboard = {}
    for index in new_tournament.players_index:
        scoreboard[new_tournament.players_index[index]] = 0

    # Play the rounds
    for t in range(new_tournament.nb_turn):
        print_menu(f'Execution of round number {str(t + 1)}', '\n')
        # creation of a new round
        turn = create_round(t)
        # find the current ranking
        current_classification = current_ranking(new_tournament.players_index, scoreboard, t)
        # generate matches
        list_match = create_match(current_classification)

        for m in range(len(list_match)):
            # enter the results of the matches
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
        new_tournament.rounds_list.append([turn.name, turn.start, turn.end, turn.match_list])

    # save tournament
    db_insert('existing_tournaments', serialized_tournament(new_tournament))
    print_menu('Tournament saved', '\n', '\n')

    # update the ranking
    ranking_update(scoreboard)

    # show ranking
    print_menu('New ranking', '\n')
    sorted_ranking = sorted(db_get('known_players', 'all'), key=lambda ranking: ranking['ranking'])
    for sort in range(len(sorted_ranking)):
        print_board(f'{str(sorted_ranking[sort]["name"])}', f'{str(sorted_ranking[sort]["ranking"])}')
    return


def players_selection():
    # selection of 8 players
    list_players = []
    for n in range(8):
        print_menu(f'Select player number {str(n + 1)}', '\n')
        selected_player = player_select('known_players', list_players)

        # creation of a new player
        if selected_player == 'new':
            tournament_player = create_player()
            # save new player
            db_insert('known_players', serialized_player(tournament_player))
            selected_player = db_get('known_players', 'index')

        list_players.append(selected_player)
    return list_players


def player_select(table, chosen_players):  # Selection of player
    # get all known players
    player_list = db_get(table, 'all')
    player_choice = '-1'
    while player_choice == '-1':
        # initialize available players
        player_listing = []
        print_menu('List of available players:')
        for a, elt in enumerate(player_list):
            # exclude players already chosen
            if str(a + 1) not in chosen_players:
                print_info(f'{str(a + 1)}: {elt["name"]} ranking: {elt["ranking"]}')
                player_listing.append(str(a + 1))
        # choose a player
        menu_choice = ""
        while menu_choice not in ('1', '2'):
            menu_choice = input_data('Select an available player (1) or add a new player (2): ', '\n')
            if menu_choice == '1':
                # test the available players
                while player_choice not in player_listing:
                    player_choice = input_data('Select a player number: ')
            elif menu_choice == '2':
                player_choice = 'new'
    return player_choice


def current_ranking(players_nb, actual_scoreboard, turn_nb):
    actual_ranking = []
    for c in range(len(players_nb)):
        if turn_nb == 0:  # take the known ranking
            actual_ranking.append([players_nb[c], db_get('known_players', 'ranking', c)])
        else:  # take the total of the score of the previous rounds
            actual_ranking.append([players_nb[c], actual_scoreboard[players_nb[c]]])
    return actual_ranking


def create_match(selected_players):
    match_list = []
    ranking_list = sorted(selected_players, key=lambda ranking: ranking[1])
    for index in range(len(ranking_list) // 2):
        player1 = ranking_list[index][0]
        player2 = ranking_list[((len(ranking_list) // 2) + index)][0]
        match_list.append([player1, player2])
    return match_list


def turn_results(list_turn, num_turn):
    score = 0
    match_result = []
    print_info(f'Match number {str(num_turn + 1)}: '
               f'playerID {(list_turn[num_turn][0])} '
               f'{db_get("known_players", "name", int(list_turn[num_turn][0]))}'
               f' VS playerID {(list_turn[num_turn][1])} '
               f'{db_get("known_players", "name", int(list_turn[num_turn][1]))}', '\n')
    while score not in ('1', '2', '3'):
        print_info(f'Choose the winner of the match:'
                   f'\nType 1 for ID: {str(list_turn[num_turn][0])}'
                   f', 2 for ID: {str(list_turn[num_turn][1])}'
                   f', 3 for : Draw')
        score = input_data(f' Your choice: ', '\n')
    if score == '1':
        match_result = [1, 0]
    if score == '2':
        match_result = [0, 0]
    if score == '3':
        match_result = [1 / 2, 1 / 2]
    return match_result


def ranking_update(board):
    update_ranking = ""
    while update_ranking.lower() != 'y':
        update_ranking = input_data('Do you want to update the ranking? (Y): ', '\n')
    print_menu('Tournament scoreboard', '\n')
    for num, point in board.items():
        print_board(num, db_get('known_players', 'ranking', int(num) - 1), f'scores {str(point)}')
    print_menu('Enter the new ranking', '\n')
    # enter the new ranking
    new_ranking_list = []
    for number in board.keys():
        # check for duplicate ranks
        new_ranking = None
        while str(new_ranking) in new_ranking_list:
            # control the format
            while True:
                new_ranking = input_data(f'Please enter the new ranking of player ID {str(number)} : ')
                try:
                    new_ranking = int(new_ranking)
                    if new_ranking > 0: break
                except ValueError:
                    print_info('Please enter a positive integer!', '\n')
            new_ranking_list.append(new_ranking)
        db_update('known_players', 'ranking', new_ranking, [int(number)])
