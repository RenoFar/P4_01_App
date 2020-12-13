#! /usr/bin/env python3
# coding: utf-8


class Match:  # Definition of class Match
    """
        Class defining a match characterized by:
        - its sorted_players
        - its match_played time
        - its new_matches
        - its n
    """

    def __init__(self, sorted_players):
        """
            Constructor of the class
            :param sorted_players: list of players sorted by ank and score
        """
        self.sorted_players = sorted_players
        self.matches_generated = []
        self.n = 1
        self.generate_matches()

    def generate_matches(self):
        # we assume that players are ordered by points and rank
        # we generate all the matches considered as if all were good
        while len(self.sorted_players) != 0:
            match_envisaged = [self.sorted_players[0], self.sorted_players[self.n]]
            self.check_match_availability(match_envisaged)

    def check_match_availability(self, match_envisaged):
        # check the availability of the match
        if match_envisaged not in self.matches_generated:
            self.add_match_to_new_matches(match_envisaged)
        else:
            self.n += 1
            # the match has already been played
            # check the existence of a next player in the available list
            if self.sorted_players[self.n]:
                # 1 : take the next one
                match_envisaged = [self.sorted_players[0], self.sorted_players[self.n]]
                self.check_match_availability(match_envisaged)
            else:
                # 2: can't take the next
                # take the last match
                last_match_created = self.matches_generated[-1]
                # put the players back at the start of the list (in order)
                self.sorted_players.insert(0, last_match_created[1])
                self.sorted_players.insert(0, last_match_created[0])
                # revalidate it by taking the next player
                match_envisaged = (self.sorted_players[0], self.sorted_players[0 + self.n])
                self.check_match_availability(match_envisaged)

    def add_match_to_new_matches(self, match_to_add):
        # the players did not meet
        # then validate the match compared to that envisaged
        # add the new match to matches_generated
        self.matches_generated.append(match_to_add)
        # remove the ids of the players who have been placed
        del self.sorted_players[0]
        del self.sorted_players[self.n]
        # reinitialise n
        self.n = 1