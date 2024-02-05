import gspread
from google.oauth2.service_account import Credentials

from colorama import Fore, Back, Style, init
from os import system, name  
import time

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

def clear_terminal():
    """
    Clears all data from terminal when called
    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def main_menu():

    print(GAME_LOGO)

    print(Fore.MAGENTA + """
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
        elif user_choice == "6":
            time.sleep(4)
            clear_terminal()
            exit()
            
def main():
    """
    Main function of the program. Shows app menu, from where user can start
    and proceed use all the app functionalities.
    """
    display_menu()

main()
                                                                                                                   
 