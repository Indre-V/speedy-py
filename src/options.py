from utils.utils import return_to_menu, typing_print, clear_terminal, space
import time
from constants import *
from utils.validation import validate_response
import textwrap
import menu as commands

def view_instructions():
    """
    Displays instructions for the typing test.
    """
    print(BLUE + INSTRUCTIONS)
    return_to_menu()
3

def typing_skills_advice():
    """
    Provides tips and tricks to improve typing speed.
    """
    print(BLUE + "12 Tips and Tricks to Improve Typing Speed:\n"
          + MAGENTA + "\nPress Enter to reveal each T&T\n" 
          + RESET_COLOR)

    for tip in TIPS:
        print(tip)
        input()

    return_to_menu()


def exit_app():
    """
    Confirms with user whether they want to exit
    """
    while True:
        confirm = input(
            YELLOW + "\nAre you sure you want to quit? Y/N: \n"
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
                typing_print(EXIT_MESSAGE)
                exit()
            else:
                clear_terminal()
                commands.display_menu()
                break

