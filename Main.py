#! / usr / bin / env python3
# coding: utf-8


class Tournament:  # Definition of the Tournament class
    """Class defining a tournament characterized by:
    - v name
    - its place
    - its place
    - its number of turns
    - its list of rounds
    - its list of players
    - its time controller
    - its description """

    def __init__(self, name, place, date, mode_game, nb_turn=4, description="description"):
        """" Constructor of the class """
        self.name = name
        self.place = place
        self.date = date
        self.nb_turn = nb_turn
        self.mode_game = mode_game
        self.description = description
        self.rounds_list = []
        self.players_index = []


class Player:  # Definition of the Player class
    """Class defining a player characterized by:
    - its name
    - its firstname
    - its date of birth
    - its gender
    - its classification """

    def __init__(self, name, firstname, date_birth, gender, index, ranking):
        """ Constructor of the class """
        self.name = name
        self.firstname = firstname
        self.date_birth = date_birth
        self.gender = gender
        self.index = index
        self.ranking = ranking


class Round:  # Definition of class Round
    """Class defining a tour characterized by:
    - its name
    - its start time
    - its end time
    - its list of matches """

    def __init__(self, name, start, end=""):
        """" Constructor of the class """
        self.name = name
        self.start = start
        self.end = end
        self.match_list = []


def create_tournament():  # create the tournament
    name = ""
    place = ""
    date = ""
    game_mode = ""
    while len(name) < 1 or not name.isalnum():
        name = input("\nPlease enter the tournament name: ")
    while len(place) < 1:
        place = input("Please enter the tournament place: ")
    while len(date) < 1:
        date = input("Tournament date: ")
    description = input("Please enter the tournament Description: ")
    while True:
        nb_turn = input('the number of laps by default is 4, '
                        '\ntype another number or Enter to validate: ')
        if len(nb_turn) < 1:  # if nothing is entered
            nb_turn = 4
            break
        else:
            try:
                nb_turn = int(nb_turn)  # conversion to integer
                if nb_turn > 0:
                    print('the number of turns is changed to: ' + str(nb_turn))
                    break
            except ValueError:
                print('\nPlease enter a positive integer!')
    while game_mode.lower() not in ('bullet', 'blitz', 'fast'):
        game_mode = input("Please enter the tournament mode (bullet / blitz / quick): ")
    return Tournament(name, place, date, game_mode, nb_turn, description)


def player_select(player_list):  # Select player
    player_choice = '-1'
    while player_choice == '-1':
        player_listing = []
        print('\n ---------- List of known players: ----------')
        for a, elt in enumerate(player_list):
            print(str(a) + ': ' + str(elt))
            player_listing.append(str(a))
        menu_choice = ""
        while menu_choice not in ('1', '2'):
            menu_choice = input('\nSelect a known player: 1'
                                '\nAdd a new player: 2'
                                '\nYour choice: ')
            if menu_choice == '1':
                while player_choice not in player_listing:
                    player_choice = input('Select a player number: ')
            elif menu_choice == '2':
                player_choice = 'new'
    return player_choice


def create_player(index):
    name = ""
    firstname = ""
    birthdate = ""
    gender = ""
    ranking = 0
    while len(name) < 1 or not name.isalnum():
        name = input("\nPlease enter player name: ")
    while len(firstname) < 1 or not firstname.isalnum():
        firstname = input("Please enter the player's firstname: ")

    birthdate = input("Please enter player's date of birth: ")

    while gender.lower() not in ('f', 'm'):
        gender = input("Please enter the player's gender (F / M): ")
    while True:
        ranking = input("Please enter player ranking: ")
        try:
            ranking = int(ranking)
            if ranking > 0: break
        except ValueError:
            print('\nPlease enter a positive integer!')
    return Player(name, firstname, birthdate, gender, index, ranking)


def create_round(number_turn):
    name = "round " + str(number_turn + 1)
    start = "start"
    end = ""
    return Round(name, start, end)


def create_match(selected_players):
    match_list = []
    ranking_list = sorted(selected_players, key=lambda ranking: ranking[1])
    """print ('\n ranked players list:', *ranking_list, '\n')"""
    for index in range(len(ranking_list) // 2):
        player1 = ranking_list[index][0]
        player2 = ranking_list[((len(ranking_list) // 2) + index)][0]
        match_list.append([player1, player2])
    return match_list


def main():
    """Main execution function of the application"""


# initialization of variables
known_players = [['j1', 'qhh', '12', 'f', '0', 18], ['j2', 'qgth', '14', 'm', '1', 7],
                 ['j3', 'qsfh', '17', 'm', '2', 8], ['j4', 'qdhg', '7', 'm', '3', 48],
                 ['j5', 'qazeah', '36', 'f', '4', 1], ['j6', 'ararh', '16', 'm', '5', 21],
                 ['j7', 'qsfq', '3', 'm', '6', 3], ['j8', 'kjqsg', '28', 'f', '7', 9]]
existing_tournaments = [['t1', 'shqshq', '26', 'bullet', 4, 'qsdggq', ['0', '1', '2', '3', '4', '5', '6', '7'], []]]
new_tournament = create_tournament()

# players selection
"""new_tournament_player_indices = []"""
for n in range(8):
    print('\n --------- Select player number ' + str(n + 1) + ' ---------')
    selected_player = player_select(known_players)
    if selected_player == 'new':
        tournament_player = create_player(str(len(known_players)))
        known_players.append([tournament_player.name, tournament_player.firstname, tournament_player.date_birth,
                              tournament_player.gender, tournament_player.index, tournament_player.ranking])
        selected_player = tournament_player.index
    new_tournament.players_index.append(selected_player)

# make the round
scoreboard = {}  # initialization of the tournament scoreboard
for t in range(new_tournament.nb_turn):
    print('\n ---------- Execution of round number ' + str(t + 1) + ' -----------')
    round = create_round(t)

    # generate matches
    current_classification = []
    for c in range(len(new_tournament.players_index)):
        if t == 0:  # take the known ranking
            scoreboard[new_tournament.players_index[c]] = 0
            current_classification.append([new_tournament.players_index[c],
                                           known_players[int(new_tournament.players_index[c])][5]])
        else:  # take the total score of the previous rounds
            current_classification.append([new_tournament.players_index[c],
                                           scoreboard[new_tournament.players_index[c]]])
    list_match = create_match(current_classification)

    # enter the results
    for m in range(len(list_match)):
        score = 0
        print('\nMatch number ' + str(m + 1) + ' : ' + str(list_match[m]))
        while score not in ('1', '2', '3'):
            score = input('Choose the winner of the match'
                          '\n type 1 for: ' + str(list_match[m][0]) +
                          '\n type 2 for: ' + str(list_match[m][1]) +
                          '\n type 3 for: Draw'
                          '\n your choice: ')
        if score == '1':
            round.match_list.append(([list_match[m][0], 1], [list_match[m][1], 0]))
            scoreboard[list_match[m][0]] += 1
        if score == '2':
            round.match_list.append(([list_match[m][0], 0], [list_match[m][1], 1]))
            scoreboard[list_match[m][1]] += 1
        if score == '3':
            round.match_list.append(([list_match[m][0], 1 / 2], [list_match[m][1], 1 / 2]))
            scoreboard[list_match[m][0]] += 1 / 2
            scoreboard[list_match[m][1]] += 1 / 2
    print(round.match_list)

    # finish the turn
    next_turn = ""
    while next_turn.lower() != 'y':
        next_turn = input('\nDo you want to validate the turn? (Y): ')
    round.end = "end"
    new_tournament.rounds_list.append([round.name, round.start, round.end, round.match_list])

# save tournament
print('\n ---------- Tournament saved ----------- \n')
existing_tournaments.append([new_tournament.name, new_tournament.place, new_tournament.date,
                             new_tournament.mode_game, new_tournament.nb_turn,
                             new_tournament.description, new_tournament.players_index,
                             new_tournament.rounds_list])

# update the ranking
update_ranking = ""
while update_ranking.lower() != 'y':
    update_ranking = input('\nDo you want to update the ranking? (Y): ')

print('\n---------- tournament scoreboard -----------')
for num, point in scoreboard.items():
    print("player {} ranked {} scores {}.".format(num, str(known_players[int(num)][5]), point))

print('\n ---------- Enter the new ranking -----------')
for number in scoreboard.keys():
    while True:
        new_ranking = input("Please enter the new ranking of player number " + str(number) + " : ")
        try:
            new_ranking = int(new_ranking)
            if new_ranking > 0: break
        except ValueError:
            print('\nPlease enter a positive integer!')
    known_players[int(number)][5] = new_ranking

# show ranking
print('\n ---------- New ranking -----------')
sorted_ranking = sorted(known_players, key=lambda ranking: ranking[5])
for sort in range(len(sorted_ranking)):
    print('N° {} of the ranking: player {}'.format(str(sorted_ranking[sort][5]), sorted_ranking[sort][4]))

if __name__ == "__main__":
    main()
