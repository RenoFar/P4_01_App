#! /usr/bin/env python3
# coding: utf-8


from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from controllers.player_controller import PlayerController
from controllers.builder_controller import BuilderController
from views.menu_view import MenuView


class MainController(BuilderController):
    """
        Class grouping together all the Main menu controllers
    """

    def __init__(self, message=None):
        """
            Constructor of the class
        """
        super().__init__(message)
        self.menu_list()

    def menu_list(self):
        """
            Main menu
        """
        while True:
            MenuView.print_menu(' Main menu ')
            self.input_service.message = (
                '\nExecute a new tournament: enter (1)\n'
                'Continue an unfinished tournament: enter (2) \n'
                'Update the actual ranking: enter (3) \n'
                'Show the reports: enter (4) \n'
                'Quit the application: enter (5) \n'
                'Please enter your choice: '
            )
            menu_choice = self.input_service.lower_not_in(
                ('1', '2', '3', '4', '5')
            )
            if menu_choice == '1':
                TournamentController().tournament_execution()
            elif menu_choice == '2':
                t_choice = TournamentController().choose_tournament()
                if t_choice is None:
                    MenuView.print_menu('any tournament')
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
