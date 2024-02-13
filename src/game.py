from wonderwords import RandomSentence
import time
import datetime
import curses
import uuid
from curses import wrapper
from utils.validation import validate_response
from api.spreadsheet import *
import menu as commands


def initialize_colors():

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)


def start_test(stdscr):
    """
    Run the typing speed test game.
    """    
    initialize_colors()
    username = ask_name(stdscr)
    
    paragraph = create_paragraph()
    display_text(stdscr, paragraph, "")
    stdscr.refresh()
    welcome_message = f"Welcome to the typing test, {username}!\n"
    time_start = time.time()
    input_text = ""
    stdscr.addstr(0, 0, welcome_message, 
                  curses.color_pair(1) | curses.A_BOLD)
    while True:
        key = stdscr.getkey()
        if key == "\n":
            break
        elif key == "KEY_BACKSPACE" or ord(key) == 127:
            if input_text:
                input_text = input_text[:-1]
        else:
            input_text += key

        stdscr.erase()
        stdscr.addstr(0, 0, welcome_message, 
                  curses.color_pair(1) | curses.A_BOLD)
        display_text(stdscr, paragraph, input_text)
        stdscr.refresh()

    show_results(stdscr, username, input_text, paragraph, time_start)


def display_text(stdscr, target, current):
    stdscr.addstr(2, 0, "Start typing the following paragraph now:", 
                  curses.color_pair(5) | curses.A_BOLD)
    stdscr.addstr(4, 0, target)  

    for i, char in enumerate(current):
        correct_char = target[i]
        if char == correct_char:
            stdscr.addch(4, i, char, curses.color_pair(1) | curses.A_BOLD)  
        else:
            stdscr.addch(4, i, char, curses.color_pair(2) | curses.A_BOLD) 


def ask_name(stdscr):
    """
    The function gets the name of the player using curses.
    """
    curses.echo()  
    stdscr.erase()
    stdscr.addstr("Please enter your name (minimum 2 characters):\n",
                curses.color_pair(4) | curses.A_BOLD)
    stdscr.refresh()
    
    while True:
        player_name = stdscr.getstr().decode("utf-8")
        if len(player_name) >= 2:
            stdscr.erase()
            curses.noecho() 
            return player_name
        else:
            stdscr.erase()
            stdscr.addstr(0, 0,"Name should have a minimum of two characters.\n",
                         curses.color_pair(2) | curses.A_BOLD)
            stdscr.addstr(2, 0,"Please try again. Enter your name:\n",
                         curses.color_pair(4) | curses.A_BOLD )
            stdscr.refresh()


def create_paragraph():
    """
    Generate a random paragraph of 2 random sentences.
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

    result_line1 = "The test is now complete. Your results are as follows:\n"
    result_line2 = f"Accuracy: {accuracy}%   WPM: {wpm}"
   
    stdscr.erase()
    stdscr.addstr(result_line1, curses.color_pair(1) | curses.A_BOLD)
    stdscr.addstr(2, 0, result_line2 + "\n\n", 
                  curses.color_pair(3) | curses.A_BOLD)


    if wpm < 10:
        stdscr.addstr(
        "\nYour typing speed is quite slow. "
        "You may want to focus on accuracy and practice more.",
        curses.color_pair(6)| curses.A_BOLD
        )
    elif wpm < 30:
        stdscr.addstr(
           "\nYour typing speed is average. "
            "Keep practicing to improve your speed and accuracy.",
            curses.color_pair(4)| curses.A_BOLD
        )
    else:
        stdscr.addstr(
            "\nCongratulations! You have a good typing speed. "
            "Keep practicing to maintain and improve it.",
            curses.color_pair(1) | curses.A_BOLD
        )

    prompt_save_test(stdscr, username, accuracy, wpm)


def prompt_save_test(stdscr, username, accuracy, wpm):
    """
    Prompt the user to save the test results or return to the main menu.
    """
    while True:
        
        stdscr.addstr(
            9, 0,
            "\nWould you like to save the test results? Y/N: ",
            curses.color_pair(4)| curses.A_BOLD
        )
        stdscr.refresh()

        key = stdscr.getch()
        stdscr.addstr(chr(key))
        stdscr.refresh()

        key = chr(key).lower() if isinstance(key, int) else key.lower()

        if key == "y":
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_data(stdscr, [username, current_time, accuracy, wpm], 'Leaderboard')

        elif key == "n":
            curses.endwin()
            time.sleep(1)
            commands.display_menu()
            break

        else:
            stdscr.addstr(
                7, 0,
                "\nInvalid input. Please enter 'Y' or 'N'.",
                curses.color_pair(2) | curses.A_BOLD
            )
            stdscr.refresh()


def save_data(stdscr, data, display_board):
    """
    Appends a new row to a worksheet in a Google Sheets document.
    """
    unique_id = str(uuid.uuid4())[:3] 
    data_with_id = [unique_id] + data  

    worksheet = SHEET.worksheet(display_board)
    worksheet.append_row(data_with_id)

    stdscr.erase()
    stdscr.addstr(2, 0,"{} worksheet updated!\n".format(display_board))
    stdscr.addstr(4, 0,"Press any key to return to Main Menu...", curses.color_pair(1)
                 | curses.A_BOLD)
    stdscr.getch()
    curses.endwin()
    commands.display_menu()
    return

def pract_accuracy(stdscr):
    paragraph = create_paragraph()
    initialize_colors()

    stdscr.addstr(2, 0, "Start typing the following paragraph now:", 
                  curses.color_pair(5) | curses.A_BOLD)
    stdscr.addstr(4, 0, paragraph)

    input_text = ""
    for i, char in enumerate(paragraph):
        stdscr.addch(4, i, char)

    while True:
        key = stdscr.getch()

        if key == ord('\n'):
            break
        elif key == curses.KEY_BACKSPACE or key == 127:
            if input_text:
                input_text = input_text[:-1]
        else:
            input_text += chr(key)

        for i, (typed_char, correct_char) in enumerate(zip(input_text, paragraph)):
            if typed_char == correct_char:
                stdscr.addch(4, i, typed_char, curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.addch(4, i, typed_char, curses.color_pair(2) | curses.A_BOLD)
        stdscr.refresh()

    accuracy = calculate_accuracy(input_text, paragraph)
    result_message = "\nCongratulations! Your accuracy is 100%." if accuracy == 100 else "\nYour accuracy is {}%.".format(accuracy)
    stdscr.addstr(7, 0, result_message, curses.color_pair(1) | curses.A_BOLD)

    while True:
        stdscr.addstr(9, 0, "\nWould you like to try again? Y/N:", 
                      curses.color_pair(4) | curses.A_BOLD)
        stdscr.refresh()

        key = stdscr.getch()
        key = chr(key).lower() if isinstance(key, int) else key.lower() 

        if key == "y":
            stdscr.erase()
            pract_accuracy(stdscr) 
        elif key == "n":
            stdscr.erase()
            curses.endwin()
            time.sleep(1)
            commands.display_menu()
            break
        else:
            stdscr.addstr(
                7, 0,
                "\nInvalid input. Please enter 'Y' or 'N'.",
                curses.color_pair(2) | curses.A_BOLD
            )
            stdscr.refresh()

def run_typing_test():
    wrapper(start_test)

def pract_acc():
    wrapper(pract_accuracy)

   

