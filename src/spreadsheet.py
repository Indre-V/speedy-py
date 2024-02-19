import gspread
from google.oauth2.service_account import Credentials
import time
import getpass
from prettytable import PrettyTable
from src.constants import *
from src.utils import *

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('leaderboard')

display_board = SHEET.worksheet('Leaderboard')

data = display_board.get_all_values()


def fetch_data_from_spreadsheet():
    """
    Fetches data from the 'Leaderboard' worksheet in the spreadsheet.
    Returns a list of lists representing the rows and columns of the worksheet.
    """
    refresh = SHEET.worksheet('Leaderboard')
    return refresh.get_all_values()


def view_leaderboard():
    """
    Top 10 results in the spreadsheet.
    Prompts user to delete result.
    """
    while True:
        data = fetch_data_from_spreadsheet()
        data_sorted = sorted(data[1:], key=lambda x: int(x[4]), reverse=True)[:10]

        headers = data[0]

        table = PrettyTable(headers)

        for row in data_sorted:
            table.add_row(row)

        if len(data) <= 1:
            print(RED + "No records found in the Leaderboard.")
            return_to_menu()
            return
        else:
            print(table)

        prompt = input(RED + "Would you like to delete a result? Y/N: "
                       + RESET_COLOR)

        if prompt.lower() == 'y':
            space()
            delete_results()
            break 
        elif prompt.lower() == 'n':
            return_to_menu()
            break  
        else:
            space()
            print(RED + "Invalid response. Please enter 'Y' or 'N'."
                "\nWait for the table to reload ..." + RESET_COLOR)
            time.sleep (2)
            clear_terminal()
            view_leaderboard()


def delete_results():
    """
    Searches for ID and deletes result.
    Displays updated leaderboard.
    """
    entry_id = input(YELLOW + "Enter the ID of the entry you want to delete: "
                     + RESET_COLOR)
    space()

    for row in data:
        if row[0] == entry_id:

            row_index = data.index(row) + 1
            display_board.delete_rows(row_index)
            print(GREEN + f"Entry with ID '{entry_id}' deleted successfully.")
            space()
            print("Loading updated Leaderboard ....")
            time.sleep(2)
            clear_terminal()
            view_leaderboard()
            return

    print(RED + f"No entry found with ID '{entry_id}'.")
    space()
    print(YELLOW + "Hit enter to reload the table")
    getpass.getpass(prompt="")
    clear_terminal()
    view_leaderboard()
