
from utils.utils import clear_terminal
from colorama import Fore, Style


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
            color_red
            + '\nIncorrect input, please enter "Y" or "N".\n'
            + Style.RESET_ALL
        )

