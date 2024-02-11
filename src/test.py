from colorama import Fore, Style, init
from wonderwords import RandomSentence
import time
from datetime import datetime
import curses
from curses import wrapper
from utils.validation import validate_response
from api.spreadsheet import save_data
import menu as commands

# Initialize Colorama
init(autoreset=True)

def start_test(stdscr):
    """
    Run the typing speed test game.
    """
    init()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    username = ask_name(stdscr)
    paragraph = create_paragraph()
    stdscr.clear()
    stdscr.addstr(Fore.LIGHTBLUE_EX + "Type the following paragraph: \n\n")
    stdscr.addstr(paragraph)
    stdscr.refresh()

    time_start = time.time()

    input_text = ""
    while True:
        key = stdscr.getkey()
        if key == "\n":
            break
        elif ord(key) == 27:  # ESC key to exit
            return
        elif key == "KEY_BACKSPACE" or ord(key) == 127:
            if input_text:
                input_text = input_text[:-1]
        else:
            input_text += key

        stdscr.clear()
        stdscr.addstr(Fore.LIGHTGREEN_EX + "Start Typing Now >>>\n")
        display_text(stdscr, paragraph, input_text)
        stdscr.refresh()

    show_results(stdscr, username, input_text, paragraph, time_start)



def display_text(stdscr, target, current):
    stdscr.addstr(0, 0, target)  # Display target text in default color
    stdscr.addstr(1, 0, "Your input: ")

    for i, char in enumerate(current):
        correct_char = target[i]
        if char == correct_char:
            stdscr.addch(char, curses.color_pair(1))  # Display correct character in green
        else:
            stdscr.addch(char, curses.color_pair(2))  # Display incorrect character in red

    stdscr.refresh()


def ask_name(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.addstr("Enter your username: ")
    stdscr.refresh()
    username = stdscr.getstr().decode("utf-8")
    curses.noecho()
    return username

def create_paragraph():
    """
    Generate a random paragraph of three random sentences.
    """
    random_sentences = [RandomSentence().sentence() for _ in range(2)]
    paragraph = " ".join(random_sentences)
    return paragraph

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

    num_correct_words = sum(a == b for a, b in zip(input_words, paragraph_words))
    accuracy_percentage = (num_correct_words / len(paragraph_words)) * 100

    return round(accuracy_percentage, 1)

def show_results(stdscr, username, input_text, paragraph, time_start):
    """
    Display the results of time taken, accuracy, and WPM.
    """
    total_time = time.time() - time_start
    accuracy = calculate_accuracy(input_text, paragraph)
    wpm = calculate_wpm(input_text, total_time, accuracy)
    results = (
        "\n" + f"Accuracy: {accuracy}%   WPM: {wpm}"
    )
    stdscr.clear()
    stdscr.addstr(Fore.LIGHTBLUE_EX + results + "\n\n")

    if wpm < 10:
        stdscr.addstr(
            Fore.LIGHTMAGENTA_EX
            + "\nYour typing speed is quite slow. "
              "You may want to focus on accuracy and practice more."
        )
    elif wpm < 30:
        stdscr.addstr(
            Fore.LIGHTYELLOW_EX
            + "\nYour typing speed is average. "
              "Keep practicing to improve your speed and accuracy."
        )
    else:
        stdscr.addstr(
            Fore.LIGHTGREEN_EX
            + "\nCongratulations! You have a good typing speed. "
              "Keep practicing to maintain and improve it."
        )

    stdscr.addstr("\n\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getch()

    prompt_save_test(stdscr, username, accuracy, wpm)

def prompt_save_test(stdscr, username, accuracy, wpm):
    """
    Prompt the user to save the test results or return to the main menu.
    """
    stdscr.clear()
    stdscr.addstr(
        Fore.LIGHTYELLOW_EX
        + "\nWould you like to save the test results? Y/N: "
        + Style.RESET_ALL
    )
    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        if key.lower() == "y":
            save_data([username, datetime.now(), accuracy, wpm], 'Leaderboard')
            curses.endwin()
            commands.display_menu()
        elif key.lower() == "n":
            curses.endwin()
            commands.display_menu()
        elif ord(key) == 27:  # ESC key to exit
            return



def run_typing_test():
    wrapper(start_test)
