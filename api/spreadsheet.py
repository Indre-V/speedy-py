import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
from utils.utils import typing_Print
import uuid
import time


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
    typing_Print(f'Update of {display_board} worksheet in progress' + "\n")
    typing_Print('... \n')
    typing_Print('... \n')
    typing_Print(f'{display_board} worksheet updated!')
    time.sleep(3)
    clear_terminal()