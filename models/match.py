#! /usr/bin/env python3
# coding: utf-8


class Match:
    """
        Class defining a match characterized by:
        - its sorted_players
        - its match_played time
        - its new_matches
        - its n
    """

    def __init__(self, sorted_players, match_played):
        """
            Constructor of the class
            :param sorted_players: list of players sorted by ank and score
        """
        self.sorted_players = sorted_players
        self.match_played = match_played
        self.match_generated = []
        self.n = 1
        self.generate_matches()

    def generate_matches(self):
        """
            Create match from the lists of match played
            and the sorted players ID
        """
        # we assume that players are ordered by points and rank
        # generate all the matches considered as if all were good
        print(f'self.sorted_players: {self.sorted_players}')
        while len(self.sorted_players) != 0:
            match_envisaged = [self.sorted_players[0],
                               self.sorted_players[self.n]
                               ]
            self.check_match_availability(match_envisaged)

    def check_match_availability(self, match_envisaged):
        """
            Check the feasibility of the match
            :param match_envisaged: match to test
        """
        # check the availability of the match
        if match_envisaged not in self.match_played:
            self.add_match_to_new_matches(match_envisaged)
        else:
            self.n += 2
            # the match has already been played
            # check the existence of a next player in the available list
            if self.sorted_players[self.n]:
                # 1 : take the next one
                match_envisaged = [self.sorted_players[0],
                                   self.sorted_players[self.n]
                                   ]
                self.check_match_availability(match_envisaged)
            else:
                # 2: can't take the next
                # take the last match
                last_match_created = self.match_generated[-1]
                # put the players back at the start of the list (in order)
                self.sorted_players.insert(0, last_match_created[1])
                self.sorted_players.insert(0, last_match_created[0])
                # revalidate it by taking the next player
                match_envisaged = (
                    self.sorted_players[0],
                    self.sorted_players[0 + self.n]
                )
                self.check_match_availability(match_envisaged)

    def add_match_to_new_matches(self, match_to_add):
        """
            Adding the the match to the match played ans generated,
            then remove the players selected & reinitialise self.n
            :param match_to_add: match validated to be played
        """
        # the players did not meet
        # then validate the match compared to that envisaged
        # add the new match to match_generated
        self.match_generated.append(match_to_add)
        # add the match generated to match_played
        self.match_played.append(match_to_add)
        # remove the ids of the players who have been placed
        del self.sorted_players[self.n]
        del self.sorted_players[0]
        # reinitialise n
        self.n = 1
