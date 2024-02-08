from src.menu import display_menu
import src.constants
import textwrap
import sys
import time
from os import system, name



def clear_terminal():
    """
    Clears all data from terminal when called
    """
    if name == "nt":
        _ = system("cls")

    else:
        _ = system("clear")


def wrap_text(text):
    """
    The function uses textwrap library to wrap long strings
    over 79 characters to the new line.
    """
    wrapper = textwrap.TextWrapper(width=79)
    wrapped_text = wrapper.fill(text=text)
    return wrapped_text


def return_to_menu():
    """
    Return the user to the beginning of the program
    """
    print(color_green + "\nHit enter to return to the main menu.\n")
    if input() == "":
        clear_terminal()

    display_menu()


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def exit_app():
    """
    Confirms with user whether they want to exit
    """
    while True:
        confirm = input(
            color_yellow + "\nAre you sure you want to quit? Y/N: \n"
            + Style.RESET_ALL
        )
        if validate_response(confirm):

            if confirm.lower() == "y":
                clear_terminal()
                print(
                    color_yellow
                    + f"Thank you for using Speedy_Py app!"
                    + Style.RESET_ALL
                )
                print(color_red + "\nTerminating..." + Style.RESET_ALL)
                exit()
            else:
                clear_terminal()
                display_menu()
                break
