#! /usr/bin/env python3
# coding: utf-8


from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from controllers.player_controller import PlayerController
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
                f'Continue an unfinished tournament: enter (2) \n'
                f'Update the actual ranking: enter (3) \n'
                f'Show the reports: enter (4) \n'
                f'Quit the application: enter (5) \n'
                f'Please enter your choice: ',
                ('1', '2', '3', '4', '5')
            )
            if menu_choice == '1':
                TournamentController().tournament_execution()
            elif menu_choice == '2':
                t_choice = TournamentController().choose_tournament()
                print(f't_choice: {t_choice}')
                print(f't_choice.doc_id: {t_choice.doc_id}')
                print(f't_choice["current_step"]: {t_choice["current_step"]}')
                print(f't_choice["current_turn"]: {t_choice["current_turn"]}')
                if t_choice is None:
                    MenuView.print_menu('No unfinished tournament')
                else:
                    TournamentController().tournament_execution(
                        t_choice.doc_id, t_choice["current_step"],
                        t_choice["current_turn"]
                    )
            elif menu_choice == '3':
                PlayerController().new_ranking()
            elif menu_choice == '4':
                ReportController()
            elif menu_choice == '5':
                MenuView.print_menu('Application closed')
                break
