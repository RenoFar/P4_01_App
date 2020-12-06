#! /usr/bin/env python3
# coding: utf-8


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
                f'Show all the players known: enter (1)\n'
                f'Show all the Tournaments played: enter (2)\n'
                f'Show the Players: enter (3)\n'
                f'Return to the Main menu: enter (4)\n'
                f'Please enter your choice: ',
                ('1', '2', '3', '4')
            )
            if report_choice == '1':
                pass
            elif report_choice == '2':
                pass
            elif report_choice == '3':
                pass
            elif report_choice == '4':
                break
