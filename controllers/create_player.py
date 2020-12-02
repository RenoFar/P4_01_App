#! /usr/bin/env python3
# coding: utf-8


from models.player import Player
from views.input_view import *
from views.info_view import *


def create_player():
    name = ""
    firstname = ""
    birthdate = ""
    gender = ""
    while len(name) < 1 or not name.isalnum():
        name = InputView.input_data('Please enter player name: ', '\n')
    while len(firstname) < 1 or not firstname.isalnum():
        firstname = InputView.input_data('Please enter the player\'s firstname: ')

    birthdate = InputView.input_data('Please enter player\'s date of birth: ')

    while gender.lower() not in ('f', 'm'):
        gender = InputView.input_data('Please enter the player\'s gender (F / M): ')
    while True:
        ranking = InputView.input_data('Please enter player ranking: ')
        try:
            ranking = int(ranking)
            if ranking > 0:
                break
        except ValueError:
            InfoView.print_info('Please enter a positive integer!', '\n')
    return Player(name, firstname, birthdate, gender, ranking)
