from colorama import Fore, Style
from utils.utils import return_to_menu, typing_Print
import time
from src.game import create_paragraph

def view_instructions():
    """
    Displays instructions for the typing test.
    """
    instructions = """
    Instructions:

    1. You will be presented with a paragraph to type.
    2. Type the paragrah exactly as it appears.
    3. Time, accuracy and speed will be measured.
    4. After typing, press Enter to see your results.
    5. Enjoy typing!
    6. Select whether to save the result or return to the main menu.
    """
    print(Fore.LIGHTBLUE_EX + instructions)
    return_to_menu()


def typing_skills_advice():
    """
    Provides tips and tricks to improve typing speed.
    """
    print(Fore.LIGHTBLUE_EX + "12 Tips and Tricks to Improve Typing Speed:\n"
          + Fore.LIGHTMAGENTA_EX + "\nPress Enter to reveal each T&T\n" 
          + Style.RESET_ALL)

    tips = [
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
    ]

    for tip in tips:
        print(tip)
        input()

    return_to_menu()

def pract_acc():
    paragraph = create_paragraph()
    print(Fore.LIGHTBLUE_EX + "Type the following paragraph: \n")
    print(paragraph)
    input_text = input(
        Fore.LIGHTGREEN_EX + "Start Typing Now >>> \n"
        + Style.RESET_ALL)
    input_text = textwrap.fill(input_text, width=70)

    accuracy = calculate_accuracy(input_text, paragraph)
    if accuracy == 100:
        print(Fore.LIGHTGREEN_EX + "\nCongratulations! Your accuracy is 100%.")
    else:
        print(Fore.LIGHTRED_EX + "\n" + f"Your accuracy is {accuracy}%.")

    while True:
        confirm = input(
            Fore.LIGHTYELLOW_EX + "\nWould you like to try again? Y/N: \n"
            + Style.RESET_ALL
        )
        if validate_response(confirm):

            if confirm.lower() == "y":
                clear_terminal()
                pract_acc()
            else:
                clear_terminal()
                return_to_menu()
                break

def start_test():
    """
    Run the typing speed test game.
    """
    paragraph = create_paragraph()
    print(color_blue + "Type the following paragraph: \n")
    print(paragraph)

    time_start = time.time()

    input_text = input(
        color_green + "Start Typing Now >>> \n"
        + Style.RESET_ALL)

    input_text = textwrap.fill(input_text, width=70)

    show_results(input_text, paragraph, time_start)

