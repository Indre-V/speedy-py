import sys
import time
from os import system, name
import src.menu as commands
from src.constants import *
import getpass


def clear_terminal():
    """
    Clears all data from terminal when called
    """
    if name == "nt":
        _ = system("cls")

    else:
        _ = system("clear")


def return_to_menu():
    """
    Return the user to the beginning of the program
    """
    print(YELLOW + "\nHit enter to return to the main menu.")
    getpass.getpass(prompt="")
    clear_terminal()
    commands.display_menu()


def space():
    """
    Adds two blank lines
    """
    print()
    print()


def validate_response(user_input):
    """
    Validates Y/N inputs provided by the user.
    If the input is invalid, it prints feedback to the user
    """
    try:
        permitted_values = ["y", "Y", "n", "N"]
        if user_input in permitted_values:
            return True
        else:
            raise ValueError
    except ValueError:
        clear_terminal()
        print(
            RED + '\nIncorrect input, please enter "Y" or "N".\n'
            + RESET_COLOR
        )
