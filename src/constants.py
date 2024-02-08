from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Define color constants
COLOR_BLUE = Fore.BLUE + Style.BRIGHT
COLOR_CYAN = Fore.CYAN + Style.BRIGHT
COLOR_YELLOW = Fore.YELLOW + Style.BRIGHT
COLOR_RED = Fore.RED + Style.BRIGHT
COLOR_GREEN = Fore.GREEN + Style.BRIGHT
COLOR_MAGENTA = Fore.MAGENTA + Style.BRIGHT

GAME_LOGO = (

    color_yellow
    + """
    ███████ ██████  ███████ ███████ ██████  ██    ██       ██████  ██    ██
    ██      ██   ██ ██      ██      ██   ██  ██  ██        ██   ██  ██  ██
    ███████ ██████  █████   █████   ██   ██   ████   █████ ██████    ████
         ██ ██      ██      ██      ██   ██    ██          ██         ██
    ███████ ██      ███████ ███████ ██████     ██          ██         ██
    """
    + "\nWelcome! Here you can learn to type faster and test your skills!"
)