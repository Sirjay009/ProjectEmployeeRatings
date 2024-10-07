import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("employee_ratings")

#scores = SHEET.worksheet("employee_survey_data")
#data = scores.get_all_values()
#print(data)

def get_scores_data():
    """
    Get scores figures input from the user.
    Run a while loop to collect a valid string of data from
    the user via the terminal. The loop will repeatedly
    request data until it is valid
    """
    print("Please enter your score ratings")
    print("Data should be three numbers seperated by commas")
    print("Data value should be between the range of 0-5")
    print("Example: 0,3,5\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_scores_data()
