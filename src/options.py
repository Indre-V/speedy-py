from utils.utils import return_to_menu, typing_print, clear_terminal, space
import time
from constants import *
from src.game import create_paragraph
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

def pract_acc():
    paragraph = create_paragraph()
    print(BLUE + "Type the following paragraph: \n")
    print(paragraph)
    input_text = input(
        GREEN + "Start Typing Now >>> \n"
        + RESET_COLOR)
    input_text = textwrap.fill(input_text, width=70)

    accuracy = calculate_accuracy(input_text, paragraph)
    if accuracy == 100:
        print(GREEN + "\nCongratulations! Your accuracy is 100%.")
    else:
        print(RED + "\n" + f"Your accuracy is {accuracy}%.")

    while True:
        confirm = input(
            YELLOW + "\nWould you like to try again? Y/N:"
            + RESET_COLOR
        )
        if validate_response(confirm):

            if confirm.lower() == "y":
                clear_terminal()
                pract_acc()
            else:
                clear_terminal()
                return_to_menu()
                break



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

