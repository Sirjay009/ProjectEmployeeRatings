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

# scores = SHEET.worksheet("employee_survey_data")
# data = scores.get_all_values()
# print(data)


def get_scores_data():
    """
    Get scores figures input from the user.
    Run a while loop to collect a valid string of data from
    the user via the terminal. The loop will repeatedly
    request data until it is valid
    """
    while True:
        print("Please enter your score ratings")
        print("Data should be three numbers seperated by commas")
        print("Data value should be between the range of 0-5")
        print("Example: 0,3,5\n")

        data_str = input("Enter your data here: ")
        # print(f"The data provided is {data_str}")

        scores_data = data_str.split(",")

        if validate_data(scores_data):
            print("Data is valid")
            break

    return scores_data


def validate_data(values):
    """
    Use 'try/except and for loop statements to check if data is valid.
    Raise ValueError if strings cannot be converted into
    integers, if there are not exactly 3 values or if out of 0 and 5 range.
    """
    # print(values)
    try:
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}"
            )

        for value in values:
            int_value = int(value)
            if not (0 <= int_value <= 5):
                raise ValueError(f"Value {int_value} is out of range (0-5)")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet_with_employee_ratings(data):
    """
    Update employee_survey_data worksheet, add new row with 
    the list data provided.
    """
    print("Updating employee_survery_data worksheet...\n")
    scores_worksheet = SHEET.worksheet("employee_survey_data")
    scores_worksheet.append_row(data)
    print("Score ratings updated successfully.\n")


def main():
    data = get_scores_data()
    # print(data)
    scores_data = [int(num) for num in data]
    # print(scores_data)
    update_worksheet_with_employee_ratings(data)


print("Welcome to project_employee_ratings Data Automation")
main()
