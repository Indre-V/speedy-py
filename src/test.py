import curses
from curses import wrapper
import time
import random
from wonderwords import RandomSentence
import textwrap



def create_paragraph():
    """
    Generate a random paragraph of three random sentences.
    """
    random_sentences = [RandomSentence().sentence() for _ in range(2)]
    paragraph = " ".join(random_sentences)
    return paragraph + "\n"

def start_screen(stdscr):
	stdscr.erase()
	stdscr.addstr("Welcome to the Speed Typing Test!")
	stdscr.addstr("\nPress any key to begin!")
	stdscr.refresh()
	stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.erase()  # Clear the screen before displaying the text

    # Display the target text
    stdscr.addstr(0, 0, target)

    # Display the WPM below the target text
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    # Display the current input with appropriate colors
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)  # Default color for correct characters

        if char != correct_char:
            color = curses.color_pair(2)  # Color for incorrect characters

        stdscr.addstr(0, i, char, color)

    stdscr.refresh()

def wpm_test(stdscr):
	target_text = create_paragraph()
	current_text = []
	wpm = 0
	start_time = time.time()
	stdscr.nodelay(True)

	while True:
		time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

		stdscr.erase()
		display_text(stdscr, target_text, current_text, wpm)
		stdscr.refresh()

		if "".join(current_text) == target_text:
			stdscr.nodelay(False)
			break

		try:
			key = stdscr.getkey()
		except:
			continue

		if ord(key) == 27:
			break

		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
			current_text.append(key)


def test(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	start_screen(stdscr)
	while True:
		wpm_test(stdscr)
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()
		
		if ord(key) == 27:
		   break

wrapper(test)