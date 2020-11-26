#! /usr/bin/env python3
# coding: utf-8


from controllers.controllers_main import *
from views.tournament_views import *


def main():
    """Main execution function of the application"""

    # initialization of variables
    initialize_db()

    # creation of the tournament
    new_tournament = create_tournament()
    """db_insert('existing_tournaments', serialized_tournament(new_tournament))"""

    # selection of 8 players
    selected_players = players_selection()
    new_tournament.players_index.append(selected_players)

    # Play the rounds
    scoreboard = {}  # initialization of the tournament scoreboard
    for t in range(new_tournament.nb_turn):
        print_menu(f'Execution of round number {str(t + 1)}', '\n')
        # creation of a new round
        turn = create_round(t)
        # find the current ranking
        current_classification = current_ranking(new_tournament.players_index, scoreboard, t)
        # generate matches
        list_match = create_match(current_classification)

        # enter the results of the turn
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

    # save tournament
    db_insert('existing_tournaments', serialized_tournament(new_tournament))
    print_menu('Tournament saved', '\n', '\n')

    # update the ranking
    update_ranking = ""
    while update_ranking.lower() != 'y':
        update_ranking = input_data('Do you want to update the ranking? (Y): ', '\n')
    print_menu('Tournament scoreboard', '\n')
    for num, point in scoreboard.items():
        print_board(num, db_get('known_players', 'ranking', int(num) - 1), f'scores {str(point)}')
    print_menu('Enter the new ranking', '\n')
    for number in scoreboard.keys():
        while True:
            new_ranking = input_data(f'Please enter the new ranking of player number {str(number)} : ')
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
