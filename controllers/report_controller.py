#! /usr/bin/env python3
# coding: utf-8


from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from services.input_service import InputService
from views.menu_view import MenuView


class ReportController:
    """
        Class grouping together all the report controllers
    """

    def __init__(self):
        self.input_service = InputService()
        self.report_execution()

    def report_execution(self):
        while True:
            MenuView.print_menu(' Report menu ')
            report_choice = self.input_service.lower_not_in(
                f'Show all the known players: enter (1)\n'
                f'Show all the known tournaments: enter (2)\n'
                f'Return to the Main menu: enter (3)\n'
                f'Please enter your choice: ',
                ('1', '2', '3')
            )
            if report_choice == '1':
                self.show_all_players()
            elif report_choice == '2':
                self.show_tournaments()
            elif report_choice == '3':
                break

    @staticmethod
    def show_all_players():
        """
            Print a list of all the known players sorted by name then by rank
        """
        MenuView.print_menu('All players in alphabetical order')
        PlayerController.players_sorted('name')
        MenuView.print_menu('All players sorted by rank')
        PlayerController.players_sorted('ranking')

    def show_tournaments(self):
        """
            Print a list all the known tournaments sorted by ID
            then offer the possibility to see the details of a chosen one
        """
        MenuView.print_menu('Tournaments played')
        list_id = TournamentController.show_tournaments([0, 1])
        # Show the details
        show_details = self.input_service.lower_not_in(
            f'Do you want to see the tournament details (yes: Y / no: N): ',
            ('y', 'n')
        )
        if show_details == 'y':
            tournament_chosen = self.input_service.lower_not_in(
                f'Please enter the ID of the chosen tournament: ',
                list_id
            )
            self.details_tournament(tournament_chosen)

    @staticmethod
    def details_tournament(tournament_id):
        """
            Print a list all the turns & matches of a tournament chosen by ID
            :param tournament_id:  id of the chosen tournament
        """
        MenuView.print_menu(' Tournament details ')
        TournamentController.turns_details(tournament_id)
