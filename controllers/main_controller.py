#! /usr/bin/env python3
# coding: utf-8


from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from services.input_service import InputService
from views.menu_view import MenuView


class MainController:
    """
        Class grouping together all the Main menu controllers
    """

    def __init__(self):
        """
            Constructor of the class
        """
        self.input_service = InputService()
        self.menu_list()

    def menu_list(self):
        """
            Main menu
        """
        while True:
            MenuView.print_menu(' Main menu ')
            menu_choice = self.input_service.lower_not_in(
                f'Execute a new tournament: enter (1)\n'
                f'Show the reports: enter (2)\n'
                f'Quit the application: enter (3)\n'
                f'Please enter your choice: ',
                ('1', '2', '3')
            )
            if menu_choice == '1':
                TournamentController()
            elif menu_choice == '2':
                ReportController()
            elif menu_choice == '3':
                MenuView.print_menu('Application closed')
                break
