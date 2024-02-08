import src.constants
from src.utils import clear_terminal
import time

def main_menu():

    print(GAME_LOGO)

    print(
        color_magenta
        + """
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
            color_green + "Please select an option from 1 to 7 "
            "to continue: \n" + Style.RESET_ALL
        )
        clear_terminal()

        validate_range = ["1", "2", "3", "4", "5", "6", "7"]

        if option not in validate_range:
            print(color_red + "Invalid choice.")
            print(color_green + "Please choose options 1 to 7 only.")
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