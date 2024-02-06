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

def main_menu():

    print(GAME_LOGO)

    print(color_magenta + """
    1. View Instructions
    2. Start Test
    3. Practice Accuracy
    4. Tips and Tricks
    5. View Leaderboard
    6. Delete Test Results
    7. Quit
    """ + Style.RESET_ALL)

def display_menu():
    while True:
        main_menu() 
        option = input(color_green
                            + "Please select an option from 1 to 7 "
                              "to continue: "
                            + Style.RESET_ALL)
        clear_terminal()
        
        validate_range = ['1', '2', '3', '4', '5', '6', '7']
        
        if option not in validate_range:
            print(color_red + "Invalid choice.")
            print(color_green + "Please choose options 1 to 7 only.")
            time.sleep(3)
            display_menu()
         
        elif option == "1":
            view_instructions()
        elif option == "2":
            start_test()
        elif option == "3": 
            pract_acc()
        elif option == "4":
            tips_tricks()
        elif option == "5":
            view_leaderboard()
        elif option == "6":
            delete_results()
        elif option == "7":
            exit_app()

def start_test():

    """
    Run the typing speed test game.
    """
    paragraph = create_paragraph()
    print(color_blue + "Type the following paragraph:"+ "\n")
    print(paragraph)

    time_start = time.time()
    

    input_text = input("Start Typing Now >>> ")
    input_text = textwrap.fill(input_text, width=70)

    show_results(input_text, paragraph, time_start)


def create_paragraph():
    """
    Generate a random paragraph of three random sentences.
    """
    random_sentences = [RandomSentence().sentence() for _ in range(4)]
    paragraph = ' '.join(random_sentences)
    return paragraph + "\n"
    

def calculate_wpm(input_text, total_time, accuracy):
    """
    Calculate adjusted words per minute (WPM) based on the user's input, total time taken,
    and accuracy percentage.
    """
    # Calculate gross WPM based on the number of characters typed and the total time taken
    if total_time != 0:
       gross_wpm = len(input_text) * 12 / total_time
    else:
        gross_wpm = 0
    
    # Adjust WPM based on accuracy
    adjusted_wpm = max(0, gross_wpm * accuracy / 100)
    
    return round(adjusted_wpm)

def calculate_accuracy(input_text, paragraph):
    """
    Calculate the accuracy of the user's input compared to the given paragraph.
    """
    correct_chars = sum(
        1 for i, c in enumerate(input_text) 
        if i < len(paragraph) and input_text[i] == paragraph[i]
    )
    return round(correct_chars / len(paragraph) * 100, 2)


def show_results(input_text, paragraph, time_start):
    """
    Display the results of time taken, accuracy, and WPM.
    """
    total_time = time.time() - time_start
    accuracy = calculate_accuracy(input_text, paragraph)
    wpm = calculate_wpm(input_text, total_time, accuracy)
    results ="\n" + f"Time: {round(total_time)} secs   Accuracy: {accuracy}%   WPM: {wpm}"
    print(color_blue+results)
     # Additional feedback based on WPM performance
    if wpm < 10:
        print(color_magenta+"\nYour typing speed is quite slow. You may want to focus on accuracy and practice more.")
    elif wpm < 30:
        print(color_blue+"\nYour typing speed is average. Keep practicing to improve your speed and accuracy.")
    else:
        print(color_green+"\nCongratulations! You have a good typing speed. Keep practicing to maintain and improve it.")
    
    prompt_save_test()


def prompt_save_test():
    """
    Prompt the user to save the test results or return to the main menu.
    """
    while True:
        confirm = input(color_yellow
                        + "\nWould you like to save the test results? Y/N: "
                        + Style.RESET_ALL)
        if validate_response(confirm):
            if confirm.lower() == "y":
                clear_terminal()
                save_data()
                display_menu()
            else:
                clear_terminal()
                display_menu()
                break
    

def exit_app():
    """
    confirms with user whether they want to exit
    """
    while True:
        confirm = input(color_yellow
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


def main():
    """
    Main function of the program. Shows application menu, from where user can start
    and proceed use all the app functionalities.
    """
    display_menu()

main()