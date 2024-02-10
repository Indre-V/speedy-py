from colorama import Fore, Style, init
from wonderwords import RandomSentence
import time
from datetime import datetime
import constants
from utils.validation import validate_response
from utils.utils import clear_terminal, wrap_text, ask_name
from api.spreadsheet import save_data
import menu as commands


def create_paragraph():
    """
    Generate a random paragraph of three random sentences.
    """
    random_sentences = [RandomSentence().sentence() for _ in range(4)]
    paragraph = " ".join(random_sentences)
    return paragraph + "\n"


def calculate_wpm(input_text, total_time, accuracy):
    """
    Calculate adjusted words per minute (WPM) based on the user's input,
    total time taken,
    and accuracy percentage.
    """
    if total_time != 0:
        gross_wpm = len(input_text) * 12 / total_time
    else:
        gross_wpm = 0

    adjusted_wpm = max(0, gross_wpm * accuracy / 100)

    return round(adjusted_wpm)


def calculate_accuracy(input_text, paragraph):
    """
    Calculate the accuracy of the user's input compared to the given paragraph.
    """

    input_words = input_text.split()
    paragraph_words = paragraph.split()

    num_correct_words = sum(
       a == b for a, b in zip(input_words, paragraph_words)
    )
    accuracy_percentage = (num_correct_words / len(paragraph_words)) * 100

    return round(accuracy_percentage, 1)


def show_results(username, input_text, paragraph, time_start):
    """
    Display the results of time taken, accuracy, and WPM.
    """
    total_time = time.time() - time_start
    accuracy = calculate_accuracy(input_text, paragraph)
    wpm = calculate_wpm(input_text, total_time, accuracy)
    results = (
        "\n" + f"Accuracy: {accuracy}%   WPM: {wpm}"
    )
    print(Fore.LIGHTBLUE_EX + results)

    if wpm < 10:
        print(
            Fore.LIGHTMAGENTA_EX
            + "\nYour typing speed is quite slow."
              "You may want to focus on accuracy and practice more."
        )
    elif wpm < 30:
        print(
            Fore.LIGHTYELLOW_EX
            + "\nYour typing speed is average."
              "Keep practicing to improve your speed and accuracy."
        )
    else:
        print(
            Fore.LIGHTGREEN_EX
            + "\nCongratulations! You have a good typing speed."
              "Keep practicing to maintain and improve it."
        )

    prompt_save_test(username, accuracy, wpm)


def prompt_save_test(username, accuracy, wpm):
    """
    Prompt the user to save the test results or return to the main menu.
    """
    while True:
        completion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = [username, completion_date, accuracy, wpm]

        confirm = input(
            Fore.LIGHTYELLOW_EX
            + "\nWould you like to save the test results? Y/N: \n"
            + Style.RESET_ALL
        )
        if validate_response(confirm):
            if confirm.lower() == "y":
                clear_terminal()
                save_data(data, 'Leaderboard')
                commands.display_menu()
            else:
                clear_terminal()
                commands.display_menu()
                break