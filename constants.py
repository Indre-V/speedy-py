from colorama import Fore, Style, init


# Initialize Colorama
init(autoreset=True)
init()
MAGENTA = Fore.LIGHTMAGENTA_EX
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX 
YELLOW = Fore.LIGHTYELLOW_EX 
BLUE = Fore.LIGHTBLUE_EX 
CYAN = Fore.LIGHTCYAN_EX
RESET_COLOR = Style.RESET_ALL


GAME_LOGO = (
  
   """
    ███████ ██████  ███████ ███████ ██████  ██    ██       ██████  ██    ██
    ██      ██   ██ ██      ██      ██   ██  ██  ██        ██   ██  ██  ██
    ███████ ██████  █████   █████   ██   ██   ████   █████ ██████    ████
         ██ ██      ██      ██      ██   ██    ██          ██         ██
    ███████ ██      ███████ ███████ ██████     ██          ██         ██
    """
    + "\nWelcome! Here you can learn to type faster and test your skills!"
)

MENU = (
    """
    1. Instructions
    2. Start Test
    3. Tips and Tricks
    4. Practice Accuracy
    5. Leaderboard
    6. Quit
    """
)


INSTRUCTIONS = (
    """
    Test Instructions:

    1. You will be presented with a paragraph to type.
    2. Type the paragrah exactly as it appears.
    3. Time, accuracy and speed will be measured.
    4. After typing, press Enter to see your results.
    5. Select whether to save the result or return to the main menu.
    """
    )

TIPS = (
    "1. Touch Typing: Learn to type without looking at the keyboard.",
    "2. Proper Posture: Maintain good posture while typing.",
    "3. Finger Placement: Keep your fingers on the home row keys.",
    "4. Use All Fingers: Utilize all your fingers for typing.",
    "5. Practice Regularly: Practice typing regularly to build muscle memory.",
    "6. Start Slow: Begin by typing slowly and focus on accuracy.",
    "7. Take Breaks: Take short breaks during typing sessions.",
    "8. Use Typing Games: Engage in typing games and exercises for fun practice.",
    "9. Focus on Weak Areas: Identify and improve specific weak areas.",
    "10. Monitor Progress: Track your typing speed and accuracy over time.",
    "11. Learn Shortcuts: Familiarize yourself with keyboard shortcuts.",
    "12. Stay Relaxed: Keep your hands and fingers relaxed while typing."
    )

EXIT_MESSAGE = (
    """
    This application was developed by Indre Vilickaite
    for Diploma in Full Stack Software Development"
    at Code Institute.

    For more information...
    https://github.com/Indre-V
    https://www.linkedin.com/in/indre-vilickaite/
    """     
    )