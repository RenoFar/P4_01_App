#! /usr/bin/env python3
# coding: utf-8


from models.TableDB import TableDB
from controllers.controllers_models import *
from views.tournament_views import *


def tournament_execution():
    # Initialize DB
    table_players = TableDB('1', 'known_players')
    table_tournaments = TableDB('2', 'existing_tournaments')
    # creation of the tournament
    new_tournament = create_tournament()
    # registration in the database
    new_tournament.insert()
    print_menu('Tournament created', '\n')
    # selection of 8 players
    new_tournament.players_index = players_selection()
    # update the tournament
    table_tournaments.update('players_index', new_tournament.players_index, [int(table_players.get_last())])
    print_menu('Tournament players updating', '\n', '\n')
    # initialization of the tournament scoreboard
    scoreboard = {}
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
        new_tournament.rounds_list.append([turn.name, turn.start, turn.end, turn.match_list])
    # update the tournament
    table_tournaments.update('rounds_list', new_tournament.rounds_list, [int(table_tournaments.get_last())])
    print_menu('Tournament rounds updating', '\n', '\n')
    # update the ranking
    ranking_update(scoreboard)
    # show ranking
    print_menu('New ranking', '\n')
    players_sorted()


def players_selection():
    # selection of 8 players
    table_players = TableDB('1', 'known_players')
    list_players = []
    for n in range(8):
        print_menu(f'Select player N° {str(n + 1)}', '\n')
        selected_player = player_select(list_players)
        # creation of a new player
        if selected_player == 'new':
            tournament_player = create_player()
            # save new player
            tournament_player.insert()
            selected_player = table_players.get_last()
        list_players.append(selected_player)
    return list_players


def player_select(chosen_players):
    # get all known players
    table_players = TableDB('1', 'known_players')
    player_list = table_players.all()
    player_choice = '-1'
    while player_choice == '-1':
        # initialize available players
        player_listing = []
        print_menu('List of available players:')
        for a, elt in enumerate(player_list):
            if str(a + 1) not in chosen_players:  # exclude players already chosen
                print_info(f'{str(a + 1)}: {elt["name"]} ranking: {elt["ranking"]}')
                player_listing.append(str(a + 1))
        # choose a player
        menu_choice = ""
        while menu_choice not in ('1', '2'):
            menu_choice = input_data('Select an available player (1) or add a new player (2): ', '\n')
            if menu_choice == '1' and len(player_listing) > 0:
                while player_choice not in player_listing:  # test the available players
                    player_choice = input_data('Select a player number: ')
            elif menu_choice == '2':
                player_choice = 'new'
    return player_choice


def current_ranking(players_nb, actual_scoreboard, turn_nb):
    table_players = TableDB('1', 'known_players')
    actual_ranking = []
    for c in range(len(players_nb)):
        if turn_nb == 0:  # take the known ranking
            actual_ranking.append([players_nb[c], table_players.all()[c]['ranking']])
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
    table_players = TableDB('1', 'known_players')
    score = 0
    match_result = []
    # show the match details
    print_info(f'Match N° {str(num_turn + 1)}: '
               f'playerID {(list_turn[num_turn][0])} '
               f'{table_players.search_by("name", int(list_turn[num_turn][0]) - 1)}'
               f' -VS- playerID {(list_turn[num_turn][1])} '
               f'{table_players.search_by("name", int(list_turn[num_turn][1]) - 1)}', '\n')
    # choose the result
    while score not in ('1', '2', '3'):
        print_info(f'Choose the winner of the match:'
                   f'\nType (1) for ID: {str(list_turn[num_turn][0])}'
                   f', (2) for ID: {str(list_turn[num_turn][1])}'
                   f', (3) for : Draw')
        score = input_data(f' Result: ', '\n')
    if score == '1':
        match_result = [1, 0]
    if score == '2':
        match_result = [0, 1]
    if score == '3':
        match_result = [1 / 2, 1 / 2]
    return match_result


def ranking_update(board):
    table_players = TableDB('1', 'known_players')
    update_ranking = ""
    while update_ranking.lower() != 'y':
        update_ranking = input_data('Do you want to update the ranking? (Y): ', '\n')
    # show the Tournament scoreboard
    print_menu('Tournament scoreboard', '\n')
    for num, point in board.items():
        print_board(num, table_players.search_by_rank('ranking', int(num) - 1), f'scores {str(point)}')
    # enter the new ranking
    print_menu('Enter the new ranking', '\n')
    new_ranking_list = []
    for number in board.keys():
        while True:  # control the chosen ranking
            while True:  # control the format
                new_ranking = input_data(f'New ranking of player ID {str(number)} : ')
                try:  # conversion on a positive integer for ranking
                    new_ranking = int(new_ranking)
                    if new_ranking > 0:
                        break
                except ValueError:
                    print_info('Please enter a positive integer!', '\n')
            if str(new_ranking) not in new_ranking_list:  # check for duplicate ranking
                new_ranking_list.append(str(new_ranking))
                break
            else:
                print_info(f'new ranking {str(new_ranking)} already chosen', '\n')
        # update the database
        table_players.update('ranking', new_ranking, [int(number)])


def players_sorted():
    table_players = TableDB('1', 'known_players')
    sorted_ranking = sorted(table_players.all(), key=lambda ranking: ranking['ranking'])
    for sort in range(len(sorted_ranking)):
        print_board(f'{str(table_players.all()[sort])} {sorted_ranking[sort]["name"]}',
                    f'{str(sorted_ranking[sort]["ranking"])}')
