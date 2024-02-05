import gspread
from google.oauth2.service_account import Credentials

from colorama import Fore, Back, Style, init
from os import system, name  
import time

# Initialize colorama, autoreset after each use of Colorama
init(autoreset=True)


GAME_LOGO = """
███████ ██████  ███████ ███████ ██████  ██    ██       ██████  ██    ██ 
██      ██   ██ ██      ██      ██   ██  ██  ██        ██   ██  ██  ██  
███████ ██████  █████   █████   ██   ██   ████   █████ ██████    ████   
     ██ ██      ██      ██      ██   ██    ██          ██         ██    
███████ ██      ███████ ███████ ██████     ██          ██         ██       
    """

def clear_terminal():
    """
    Clears the terminal.
    """
    #  for windows
    if name == 'nt':
        _ = system('cls')

    #  for mac and linux
    else:
        _ = system('clear')

def main_menu():

    print(GAME_LOGO)

    print(Fore.LIGHTGREEN_EX + """
    1. Start Test
    2. View Instructions
    3. Tips and Tricks
    4. View Leaderboard
    5. Delete Results
    6. Quit
    """ + Style.RESET_ALL)

def display_menu():
    while True:
        main_menu()  # prints menu
        option = input(Fore.LIGHTBLUE_EX
                            + "Please select an option from 1 to 6 "
                              "to continue: "
                            + Style.RESET_ALL)
        clear_terminal()
        
        validate_range(option, 1, 6)

        if option == "1":
            start_test()
        elif option == "2":
            view_instructions()
        elif option == "3":
            tips_tricks()
        elif option == "4":
            view_leaderboard()
        elif option == "5":
            delete_results()
        elif user_choice == "6":
            time.sleep(4)
            clear_terminal()
            exit()
            

                                                                                                                   
 