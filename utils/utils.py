import sys
import time
from os import system, name
import menu as commands
from constants import *


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
    print(YELLOW + "\nHit enter to return to the main menu.\n")
    if input() == "":
        clear_terminal()
        commands.display_menu()
    else:
        clear_terminal()
        commands.display_menu()


def typing_print(text):
    """
    Prints text gradually as if it were being typed out.
    Pressing Enter displays the full text immediately.
    """
    for character in text:
         sys.stdout.write(character)
         sys.stdout.flush()
         time.sleep(0.05)

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

