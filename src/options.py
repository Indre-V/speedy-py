from colorama import Fore, Style
from utils.utils import return_to_menu, typing_print, ask_name, clear_terminal, space
import time
from constants import TIPS, INSTRUCTIONS, EXIT_MESSAGE
from src.game import create_paragraph, show_results, calculate_accuracy
from utils.validation import validate_response
import textwrap
import menu as commands

def view_instructions():
    """
    Displays instructions for the typing test.
    """
    print(Fore.LIGHTBLUE_EX + INSTRUCTIONS)
    return_to_menu()


def typing_skills_advice():
    """
    Provides tips and tricks to improve typing speed.
    """
    print(Fore.LIGHTBLUE_EX + "12 Tips and Tricks to Improve Typing Speed:\n"
          + Fore.LIGHTMAGENTA_EX + "\nPress Enter to reveal each T&T\n" 
          + Style.RESET_ALL)

    for tip in TIPS:
        print(tip)
        input()

    return_to_menu()

def pract_acc():
    paragraph = create_paragraph()
    print(Fore.LIGHTBLUE_EX + "Type the following paragraph: \n")
    print(paragraph)
    input_text = input(
        Fore.LIGHTGREEN_EX + "Start Typing Now >>> \n"
        + Style.RESET_ALL)
    input_text = textwrap.fill(input_text, width=70)

    accuracy = calculate_accuracy(input_text, paragraph)
    if accuracy == 100:
        print(Fore.LIGHTGREEN_EX + "\nCongratulations! Your accuracy is 100%.")
    else:
        print(Fore.LIGHTRED_EX + "\n" + f"Your accuracy is {accuracy}%.")

    while True:
        confirm = input(
            Fore.LIGHTYELLOW_EX + "\nWould you like to try again? Y/N: \n"
            + Style.RESET_ALL
        )
        if validate_response(confirm):

            if confirm.lower() == "y":
                clear_terminal()
                pract_acc()
            else:
                clear_terminal()
                return_to_menu()
                break

def start_test():
    """
    Run the typing speed test game.
    """
    username = ask_name()
    paragraph = create_paragraph()
    print(Fore.LIGHTBLUE_EX + "Type the following paragraph: \n")
    print(paragraph)

    time_start = time.time()

    input_text = input(
        Fore.LIGHTGREEN_EX + "Start Typing Now >>> \n"
        + Style.RESET_ALL)

    input_text = textwrap.fill(input_text, width=70)

    show_results(username, input_text, paragraph, time_start)

def exit_app():
    """
    Confirms with user whether they want to exit
    """
    while True:
        confirm = input(
            Fore.LIGHTYELLOW_EX + "\nAre you sure you want to quit? Y/N: \n"
            + Style.RESET_ALL
        )
        if validate_response(confirm):

            if confirm.lower() == "y":
                clear_terminal()
                print(
                    Fore.LIGHTGREEN_EX
                    + f"Thank you for using Speedy_Py app!"
                    + Style.RESET_ALL
                )
                print(Fore.LIGHTRED_EX + "\nTerminating..." + Style.RESET_ALL)
                typing_print(EXIT_MESSAGE)
                exit()
            else:
                clear_terminal()
                commands.display_menu()
                break

