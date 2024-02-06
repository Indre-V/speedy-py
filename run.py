import gspread
from google.oauth2.service_account import Credentials

from colorama import Fore, Back, Style, init
from os import system, name  
import time
import textwrap
from wonderwords import RandomSentence


# Colorama colors

color_blue = Fore.BLUE+Style.NORMAL
color_cyan = Fore.CYAN+Style.BRIGHT
color_yellow = Fore.YELLOW+Style.BRIGHT
color_red = Fore.RED+Style.BRIGHT
color_green = Fore.GREEN+Style.BRIGHT
color_magenta = Fore.MAGENTA+Style.BRIGHT


# Initialize colorama, autoreset after each use of Colorama
init(autoreset=True)


GAME_LOGO = color_yellow + """
        
    ███████ ██████  ███████ ███████ ██████  ██    ██       ██████  ██    ██ 
    ██      ██   ██ ██      ██      ██   ██  ██  ██        ██   ██  ██  ██  
    ███████ ██████  █████   █████   ██   ██   ████   █████ ██████    ████   
         ██ ██      ██      ██      ██   ██    ██          ██         ██    
    ███████ ██      ███████ ███████ ██████     ██          ██         ██    
                                                     
    """ 

print(color_yellow
          + f"Welcome! Here you can learn to type faster and test your skills!")
       

def clear_terminal():
    """
    Clears all data from terminal when called
    """
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def wrap_text(text):
    """
    The function uses textwrap library to wrap long strings
    over 79 characters to the new line.
    """
    wrapper = textwrap.TextWrapper(width=79)
    wrapped_text = wrapper.fill(text=text)
    return wrapped_text

def main_menu():

    print(GAME_LOGO)

    print(color_magenta + """
    1. Start Test
    2. View Instructions
    3. Tips and Tricks
    4. View Leaderboard
    5. Delete Results
    6. Quit
    """ + Style.RESET_ALL)

def display_menu():
    while True:
        main_menu() 
        option = input(color_green
                            + "Please select an option from 1 to 6 "
                              "to continue: "
                            + Style.RESET_ALL)
        clear_terminal()
        
        validate_range = ['1', '2', '3', '4', '5', '6']
        
        if option not in validate_range:
            print(color_red + "Invalid choice.")
            print(color_green + "Please choose options 1 to 6 only.")
            time.sleep(3)
            display_menu()
         
        elif option == "1":
            start_test()
        elif option == "2":
            view_instructions()
        elif option == "3":
            tips_tricks()
        elif option == "4":
            view_leaderboard()
        elif option == "5":
            delete_results()
        elif option == "6":
            exit_app()

def start_test():

    """
    Run the typing speed test game.
    """
    paragraph = create_paragraph()
    print("Type the following paragraph:")
    print(paragraph)

    time_start = time.time()
    input_text = textwrap.fill(input_text, width=70)

    input_text = input("Start Typing Now >>> ")

    show_results(input_text, paragraph, time_start)


def create_paragraph():
    """
    Generate a random paragraph of three random sentences.
    """
    random_sentences = [RandomSentence().sentence() for _ in range(3)]
    paragraph = ' '.join(random_sentences)
    return paragraph
    

def calculate_accuracy(input_text, paragraph):
    """
    Calculate th1e accuracy of the user's input compared to the given paragraph.
    """
    correct_chars = sum(1 for i, c in enumerate(input_text) if i < len(paragraph) and input_text[i] == paragraph[i])
    return round(correct_chars / len(paragraph) * 100, 2)


def calculate_wpm(input_text, total_time):
    """
    Calculate words per minute (WPM) based on the user's input and the total time taken.
    Value 12 assumes an average word length of 5 characters plus spaces and punctuation marks
    """
    return round(len(input_text) * 12 / total_time)


def show_results(input_text, paragraph, time_start):
    """
    Display the results g time taken, accuracy, and WPM.
    """
    total_time = time.time() - time_start
    accuracy = calculate_accuracy(input_text, paragraph)
    wpm = calculate_wpm(input_text, total_time)
    results = f"Time: {round(total_time)} secs   Accuracy: {accuracy}%   WPM: {wpm}"
    print(results)


def exit_app():
    """
    confirms with user whether they want to exit
    """
    while True:
        confirm = input(Fore.LIGHTYELLOW_EX
                             + "\nAre you sure you want to quit? Y/N: "
                             + Style.RESET_ALL)
        if validate_response(confirm):

            if confirm.lower() == "y":
                clear_terminal()
                print(color_yellow
                      + f"Thank you for using Speedy_Py app!"
                      + Style.RESET_ALL)
                print(color_red + "\nTerminating..."
                                          + Style.RESET_ALL)
                exit()
            else:
                clear_terminal()
                display_menu()  
                break
        

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
        print(color_red
              + "\nIncorrect input, please enter \"Y\" or \"N\".\n"
              + Style.RESET_ALL)

           
def main():
    """
    Main function of the program. Shows application menu, from where user can start
    and proceed use all the app functionalities.
    """
    display_menu()

main()
