from src.utils import *
from src.constants import *
import src.menu as commands
import time
import getpass


def view_instructions():
    """
    Instructions for the typing test.
    """
    print(BLUE + INSTRUCTIONS)
    return_to_menu()


def typing_skills_advice():
    """
    Tips and tricks to improve typing speed.
    """
    print(BLUE + "12 Tips and Tricks to Improve Typing Speed:\n"
          + MAGENTA + "\nPress Enter to reveal each T&T\n"
          + RESET_COLOR)

    for tip in TIPS:
        print(tip)
        getpass.getpass(prompt="")

    return_to_menu()


def exit_app():
    """
    Confirms with user whether they want to exit.
    Exit Message displayed.
    """
    while True:
        confirm = input(
            YELLOW + "\nAre you sure you want to quit? Y/N:"
            + RESET_COLOR
        )
        if validate_response(confirm):

            if confirm.lower() == "y":
                clear_terminal()
                print(
                    GREEN
                    + f"Thank you for using Speedy_Py app!"
                    + RESET_COLOR
                )
                print(RED + "\nTerminating..." + RESET_COLOR)
                print(EXIT_MESSAGE)
                exit()
            else:
                clear_terminal()
                commands.display_menu()
                break
