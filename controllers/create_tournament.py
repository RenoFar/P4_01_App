#! /usr/bin/env python3
# coding: utf-8


from models.tournament import Tournament
from views.input_view import *
from views.info_view import *


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