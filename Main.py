#! /usr/bin/env python3
# coding: utf-8


from controllers.controllers_models import *
from controllers.controllers_db import *
from views.tournament_views import *


def main():
    """Main execution function of the application"""


# initialization of variables
initialize_db()

# creation of the tournament
new_tournament = create_tournament()

# selection of 8 players
for n in range(8):
    print_menu('Select player number ' + str(n + 1), '\n')
    selected_player = player_select('known_players')

    # creation of a new player
    if selected_player == 'new':
        tournament_player = create_player()
        # save new player
        db_insert('known_players', serialized_player(tournament_player))
        selected_player = db_get('known_players', 'index')

    new_tournament.players_index.append(selected_player)

# Play the rounds
scoreboard = {}  # initialization of the tournament scoreboard
for t in range(new_tournament.nb_turn):
    print_menu('Execution of round number ' + str(t + 1), '\n')

    # creation of a new round
    turn = create_round(t)

    # find the current ranking
    current_classification = []
    for c in range(len(new_tournament.players_index)):
        if t == 0:  # take the known ranking
            scoreboard[new_tournament.players_index[c]] = 0
            current_classification.append([new_tournament.players_index[c],
                                           db_get('known_players', 'ranking', c)])
        else:  # take the total of the score of the previous rounds
            current_classification.append([new_tournament.players_index[c],
                                           scoreboard[new_tournament.players_index[c]]])
    # generate matches
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
update_ranking = ""
while update_ranking.lower() != 'y':
    update_ranking = input_data('Do you want to update the ranking? (Y): ', '\n')
print_menu('Tournament scoreboard', '\n')
for num, point in scoreboard.items():
    print_board(num, db_get('known_players', 'ranking', int(num)-1), 'scores ' + str(point))
print_menu('Enter the new ranking', '\n')
for number in scoreboard.keys():
    while True:
        new_ranking = input_data('Please enter the new ranking of player number ' + str(number) + ' : ')
        try:
            new_ranking = int(new_ranking)
            if new_ranking > 0: break
        except ValueError:
            print_info('Please enter a positive integer!', '\n')
    db_update('known_players', 'ranking', new_ranking, [int(number)])

# show ranking
print_menu('New ranking', '\n')
sorted_ranking = sorted(db_get('known_players', 'all'), key=lambda ranking: ranking['ranking'])
for sort in range(len(sorted_ranking)):
    print_board(str(sorted_ranking[sort]['name']), str(sorted_ranking[sort]['ranking']))


if __name__ == "__main__":
    main()
