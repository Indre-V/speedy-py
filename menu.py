from src.options import *
from constants import GAME_LOGO
import time
from colorama import Fore, Style
from utils.utils import clear_terminal



def main_menu():

    print(GAME_LOGO)
    print(
    Fore.LIGHTMAGENTA_EX
    + 
    """
    1. View Instructions
    2. Start Test
    3. Tips and Tricks
    4. Practice Accuracy
    5. View Leaderboard
    6. Delete Test Results
    7. Quit
    """
        + Style.RESET_ALL
    )


def display_menu():
    while True:
        main_menu()
        option = input(
            Fore.LIGHTGREEN_EX + "Please select an option from 1 to 7 "
            "to continue: \n" + Style.RESET_ALL
        )
        clear_terminal()

        validate_range = ["1", "2", "3", "4", "5", "6", "7"]

        if option not in validate_range:
            print(Fore.LIGHTRED_EX+ "Invalid choice.")
            print(Fore.LIGHTGREEN_EX + "Please choose options 1 to 7 only.")
            time.sleep(3)
            display_menu()

        elif option == "1":
            view_instructions()
        elif option == "2":
            start_test()
        elif option == "3":
            typing_skills_advice()
        elif option == "4":
            pract_acc()
        elif option == "5":
            view_leaderboard()
        elif option == "6":
            delete_results()
        elif option == "7":
            exit_app()