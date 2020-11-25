#! /usr/bin/env python3
# coding: utf-8


from models.tournament import Tournament
from models.player import Player
from models.round import Round
from views.tournament_views import *


def create_tournament():  # create the tournament
    name = ""
    place = ""
    date = ""
    game_mode = ""
    while len(name) < 1 or not name.isalnum():
        name = input_data('Please enter the tournament name: ', '\n')
    while len(place) < 1:
        place = input_data('Please enter the tournament place: ')
    while len(date) < 1:
        date = input_data('Tournament date: ')
    description = input_data('Please enter the tournament description: ')
    while True:
        nb_turn = input_data('The number of laps by default is 4, '
                             '\n type another number or Enter to validate: ')
        if len(nb_turn) < 1:  # if nothing is entered
            nb_turn = 4
            break
        else:
            try:
                nb_turn = int(nb_turn)  # conversion to integer
                if nb_turn > 0:
                    print_info('The number of turns is changed to: ' + str(nb_turn))
                    break
            except ValueError:
                print_info('Please enter a positive integer!', '\n')
    while game_mode.lower() not in ('bullet', 'blitz', 'speed'):
        game_mode = input_data('Please enter the tournament mode (bullet / blitz / speed): ')
    return Tournament(name, place, date, game_mode, nb_turn, description)


def create_player():
    name = ""
    firstname = ""
    birthdate = ""
    gender = ""
    ranking = 0
    while len(name) < 1 or not name.isalnum():
        name = input_data('Please enter player name: ', '\n')
    while len(firstname) < 1 or not firstname.isalnum():
        firstname = input_data('Please enter the player\'s firstname: ')

    birthdate = input_data('Please enter player\'s date of birth: ')

    while gender.lower() not in ('f', 'm'):
        gender = input_data('Please enter the player\'s gender (F / M): ')
    while True:
        ranking = input_data('Please enter player ranking: ')
        try:
            ranking = int(ranking)
            if ranking > 0: break
        except ValueError:
            print_info('Please enter a positive integer!', '\n')
    return Player(name, firstname, birthdate, gender, ranking)


def create_round(number_turn):
    name = "round " + str(number_turn + 1)
    start = "start"
    end = ""
    return Round(name, start, end)


def create_match(selected_players):
    match_list = []
    ranking_list = sorted(selected_players, key=lambda ranking: ranking[1])
    for index in range(len(ranking_list) // 2):
        player1 = ranking_list[index][0]
        player2 = ranking_list[((len(ranking_list) // 2) + index)][0]
        match_list.append([player1, player2])
    return match_list




