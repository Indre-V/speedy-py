from src.options import *
from src.test import *
from constants import GAME_LOGO
import time
from colorama import Fore, Style
from utils.utils import clear_terminal
from api.spreadsheet import view_leaderboard
from src.test import run_typing_test



def main_menu():

    print(GAME_LOGO)
    print(
    Fore.LIGHTMAGENTA_EX
    + 
    """
    1. Instructions
    2. Start Test
    3. Tips and Tricks
    4. Practice Accuracy
    5. Leaderboard
    6. Quit
    """
        + Style.RESET_ALL
    )


def display_menu():

    while True:
        main_menu()
        option = input(
            Fore.LIGHTGREEN_EX + "Please select an option from 1 to 6"
            "to continue: \n" + Style.RESET_ALL
        )
        clear_terminal()

        validate_range = ["1", "2", "3", "4", "5", "6"]

        if option not in validate_range:
            print(Fore.LIGHTRED_EX+ "Invalid choice.")
            print(Fore.LIGHTGREEN_EX + "Please choose options 1 to 6 only.")
            time.sleep(3)
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

def view_menu ():
    display_menu()