
from utils.utils import clear_terminal
from constants import *


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

