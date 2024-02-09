import textwrap
import sys
import time
from os import system, name
from colorama import Fore, Style
import menu as commands


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
    print(Fore.LIGHTGREEN_EX + "\nHit enter to return to the main menu.\n")
    if input() == "":
        clear_terminal()
        commands.display_menu()
    else:
        clear_terminal()
        commands.display_menu()

    """
    Prints text gradually as if it were being typed out.
    Pressing Enter displays the full text immediately.
    """
def typing_Print(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def ask_name():
    '''
    The function gets the name of the player.
    '''
    player_name = input('Please enter your name.\n')
    print(f'***Welcome to the typing test {player_name}!***')
    return player_name

