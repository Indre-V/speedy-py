from src.options import *
from src.constants import *
import time
from src.utils import clear_terminal
from src.spreadsheet import view_leaderboard
from src.game import run_typing_test, pract_acc


def main_menu():
    """
    Main Menu options and logo
    """

    print(YELLOW + GAME_LOGO)
    print(MENU)


def display_menu():
    """
    Menu functions.
    Validates user input
    """

    while True:
        main_menu()
        option = input(
            GREEN + "Please select an option from 1 to 6"
            " to continue: \n" + RESET_COLOR
        )
        clear_terminal()

        validate_range = ["1", "2", "3", "4", "5", "6"]

        if option not in validate_range:
            print(RED + "Invalid choice.")
            print(GREEN + "Please choose options 1 to 6 only.")
            time.sleep(1)
            clear_terminal()
            display_menu()
        elif option == "1":
            view_instructions()
        elif option == "2":
            run_typing_test()
        elif option == "3":
            typing_skills_advice()
        elif option == "4":
            pract_acc()
        elif option == "5":
            view_leaderboard()
        elif option == "6":
            exit_app()
