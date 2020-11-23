#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB
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
    return name, place, date, game_mode, nb_turn, description


def player_select(player_list):  # Select player
    player_choice = '-1'
    while player_choice == '-1':
        player_listing = []
        print_menu('List of known players:', '\n')
        for a, elt in enumerate(player_list):
            print_info(str(a+1) + ': ' + str(elt))
            # print(str(a) + ': ' + str(elt))
            player_listing.append(str(a+1))
        menu_choice = ""
        while menu_choice not in ('1', '2'):
            menu_choice = input_data('Select a known player (1) or add a new player (2): ', '\n')
            if menu_choice == '1':
                while player_choice not in player_listing:
                    player_choice = input_data('Select a player number: ')
            elif menu_choice == '2':
                player_choice = 'new'
    return player_choice


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
    return name, firstname, birthdate, gender, ranking


def create_round(number_turn):
    name = "round " + str(number_turn + 1)
    start = "start"
    end = ""
    return name, start, end


def create_match(selected_players):
    match_list = []
    ranking_list = sorted(selected_players, key=lambda ranking: ranking[1])
    for index in range(len(ranking_list) // 2):
        player1 = ranking_list[index][0]
        player2 = ranking_list[((len(ranking_list) // 2) + index)][0]
        match_list.append([player1, player2])
    return match_list


def serialized_player(player):
    return {'name': player.name, 'firstname': player.firstname, 'date_birth': player.date_birth,
            'gender': player.gender, 'ranking': player.ranking}


def serialized_tournament(tournament):
    return {'name': tournament.name, 'place': tournament.place, 'date': tournament.date,
            'mode_game': tournament.mode_game, 'nb_turn': tournament.nb_turn,
            'description': tournament.description, 'players_index': tournament.players_index,
            'rounds_list': tournament.rounds_list}


def insert_db(table, data_dict):
    database.table(table).insert(data_dict)


def db_get(table, info, nb=None):
    if info == 'index':
        result = table.all()[len(table)].doc_id
    else:
        result = table.all()[nb][info]
    return result


def db_update(table, key, value, data_id_list):
    database.table(table).update({key: value}, doc_ids=data_id_list)


def main():
    """Main execution function of the application"""


# initialization of variables
database = TinyDB('database.json')
"""database.truncate()"""

players_table = database.table('known_players')
tournaments_table = database.table('existing_tournaments')

"""known_players = [
    {'name': 'Martin', 'firstname': 'Lucie', 'date_birth': '2000', 'gender': 'f', 'ranking': 18},
    {'name': 'Petit', 'firstname': 'Lucas', 'date_birth': '2001', 'gender': 'm', 'ranking': 7},
    {'name': 'Dubois', 'firstname': 'Samuel', 'date_birth': '2002', 'gender': 'm', 'ranking': 8},
    {'name': 'Durand', 'firstname': 'Lily', 'date_birth': '1999', 'gender': 'f', 'ranking': 12},
    {'name': 'Leroy', 'firstname': 'Alina', 'date_birth': '1995', 'gender': 'f', 'ranking': 1},
    {'name': 'Moreau', 'firstname': 'Nolan', 'date_birth': '1998', 'gender': 'm', 'ranking': 20},
    {'name': 'Garcia', 'firstname': 'Julian', 'date_birth': '1992', 'gender': 'm', 'ranking': 3},
    {'name': 'Roux', 'firstname': 'Marie', 'date_birth': '1977', 'gender': 'f', 'ranking': 9}]
existing_tournaments = [
    {'name': 't1', 'place': 'Paris', 'date': '26', 'mode_game': 'bullet', 'nb_turn': 4, 'description': 'First',
     'players_index': ['1', '2', '3', '4', '5', '6', '7', '8'], 'rounds_list': []}]

insert_db(players_table.name, known_players)
insert_db(tournaments_table.name, existing_tournaments)"""

# creation of the tournament
new_tournament_data = create_tournament()
new_tournament = Tournament(new_tournament_data[0], new_tournament_data[1], new_tournament_data[2],
                            new_tournament_data[3], new_tournament_data[4], new_tournament_data[5])

# players selection
for n in range(8):
    print_menu('Select player number ' + str(n + 1), '\n')
    selected_player = player_select(players_table)
    # creation of a new player
    if selected_player == 'new':
        tournament_player_data = create_player()
        tournament_player = Player(tournament_player_data[0], tournament_player_data[1],
                                   tournament_player_data[2], tournament_player_data[3],
                                   tournament_player_data[4])

        # save new player
        insert_db(players_table.name, serialized_player(tournament_player))
        """known_players.append([tournament_player.name, tournament_player.firstname, tournament_player.date_birth,
                              tournament_player.gender, tournament_player.index, tournament_player.ranking])"""
        selected_player = db_get(players_table, 'index')

    new_tournament.players_index.append(selected_player)

# make the rounds
scoreboard = {}  # initialization of the tournament scoreboard
for t in range(new_tournament.nb_turn):
    print_menu('Execution of round number ' + str(t + 1), '\n')
    turn_data = create_round(t)
    turn = Round(turn_data[0], turn_data[1], turn_data[2])

    # generate matches
    current_classification = []
    for c in range(len(new_tournament.players_index)):
        if t == 0:  # take the known ranking
            scoreboard[new_tournament.players_index[c]] = 0
            current_classification.append([new_tournament.players_index[c],
                                           db_get(players_table, 'ranking', c)])
        else:  # take the total score of the previous rounds
            current_classification.append([new_tournament.players_index[c],
                                           scoreboard[new_tournament.players_index[c]]])
    list_match = create_match(current_classification)

    # enter the results of the turn
    for m in range(len(list_match)):
        score = 0
        print_info('Match number ' + str(m + 1) + ' : ' + str(list_match[m]), '\n')
        while score not in ('1', '2', '3'):
            score = input_data('Choose the winner of the match'
                               '\n Type 1 for: ' + str(list_match[m][0]) +
                               '\n Type 2 for: ' + str(list_match[m][1]) +
                               '\n Type 3 for: Draw'
                               '\n Your choice: ')
        if score == '1':
            turn.match_list.append(([list_match[m][0], 1], [list_match[m][1], 0]))
            scoreboard[list_match[m][0]] += 1
        if score == '2':
            turn.match_list.append(([list_match[m][0], 0], [list_match[m][1], 1]))
            scoreboard[list_match[m][1]] += 1
        if score == '3':
            turn.match_list.append(([list_match[m][0], 1 / 2], [list_match[m][1], 1 / 2]))
            scoreboard[list_match[m][0]] += 1 / 2
            scoreboard[list_match[m][1]] += 1 / 2
    # print(turn.match_list)

    # finish the turn
    next_turn = ""
    while next_turn.lower() != 'y':
        next_turn = input_data('Do you want to validate the turn? (Y): ', '\n')
    turn.end = "end"
    new_tournament.rounds_list.append([turn.name, turn.start, turn.end, turn.match_list])

# save tournament
insert_db(tournaments_table.name, serialized_tournament(new_tournament))
"""existing_tournaments.append([new_tournament.name, new_tournament.place, new_tournament.date,
                             new_tournament.mode_game, new_tournament.nb_turn,
                             new_tournament.description, new_tournament.players_index,
                             new_tournament.rounds_list])"""
print_menu('Tournament saved', '\n', '\n')

# update the ranking
update_ranking = ""
while update_ranking.lower() != 'y':
    update_ranking = input_data('Do you want to update the ranking? (Y): ', '\n')

print_menu('Tournament scoreboard', '\n')
for num, point in scoreboard.items():
    print_board(num, db_get(players_table, 'ranking', str(num+1)), 'scores '+str(point))

print_menu('Enter the new ranking', '\n')
for number in scoreboard.keys():
    while True:
        new_ranking = input_data('Please enter the new ranking of player number ' + str(number) + ' : ')
        try:
            new_ranking = int(new_ranking)
            if new_ranking > 0: break
        except ValueError:
            print_info('Please enter a positive integer!', '\n')
    db_update(players_table, 'ranking', new_ranking, str(number))
    """known_players[int(number)][5] = new_ranking"""

# show ranking
print_menu('New ranking', '\n')
sorted_ranking = sorted(players_table.all(), key=lambda ranking: ranking['ranking'])
for sort in range(len(sorted_ranking)):
    print_board(str(sorted_ranking[sort][4]), sorted_ranking[sort][5])


if __name__ == "__main__":
    main()
