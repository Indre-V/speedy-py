import gspread
from google.oauth2.service_account import Credentials
from utils.utils import typing_print, clear_terminal, return_to_menu
import uuid
import time
from prettytable import PrettyTable


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

def save_data(data, display_board):
    """
    This function appends a new row to a worksheet in a Google Sheets document.
    """
    unique_id = str(uuid.uuid4())[:4] 
    data_with_id = [unique_id] + data  
    worksheet= SHEET.worksheet(display_board)
    worksheet.append_row(data_with_id)
    typing_print(f'Update of {display_board} worksheet in progress' + "\n")
    typing_print('... \n')
    typing_print('... \n')
    typing_print(f'{display_board} worksheet updated!')
    time.sleep(3)
    clear_terminal()

def view_leaderboard():
    """
    This function displays top 10 results in the spreadsheet
    """

    lead = SHEET.worksheet('Leaderboard')
    leaderboard = lead.get_all_values()

    leaderboard_sorted = sorted(leaderboard[1:], key=lambda x: int(x[4]), reverse=True)[:10]

    headers = leaderboard[0] 

    table = PrettyTable(headers)

    for row in leaderboard_sorted:
        table.add_row(row)

    print(table)
    return_to_menu()


    