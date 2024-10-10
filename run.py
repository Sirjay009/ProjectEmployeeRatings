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
    Convert string values to intergers.
    Raise ValueError if strings cannot be converted into
    integers, if there are not exactly 3 values or if values
    are out of the range of 0 and 5.
    """
    # print(values)
    try:
        [int(value) for value in values]
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
    scores_worksheet.insert_row([int(num) for num in data], 2)
    print("Score ratings updated successfully.\n")


def get_and_convert_column_to_integers(employee_survey_data, column_index):
    """
    Pull values from a specified column in the worksheet
    and convert them to integers.
    """
    scores_data = SHEET.worksheet(employee_survey_data)
    column_scores = scores_data.col_values(column_index)

    try:
        int_column_scores = [
            int(value) for value in column_scores if value.isdigit()
        ]

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

    return int_column_scores


def calculate_and_update_average_score_ratings(values, column_name):
    """
    Calculate the average rating for each column of
    the employee_survey_data.
    """
    print(f"Calculating {column_name} score rating...\n")
    total_column_sum = sum(values)
    entries = len(values)
    average = round(total_column_sum / entries, 3)

    return total_column_sum, average


def main():
    """
    Run all program functions
    """
    data = get_scores_data()
    # print(data)
    update_worksheet_with_employee_ratings(data)
    column_a = get_and_convert_column_to_integers("employee_survey_data", 1)
    column_b = get_and_convert_column_to_integers("employee_survey_data", 2)
    column_c = get_and_convert_column_to_integers("employee_survey_data", 3)
    sum_a, avg_a = calculate_and_update_average_score_ratings(
        column_a, "Environment Satisfaction")
    sum_b, avg_b = calculate_and_update_average_score_ratings(
        column_b, "Job Satisfaction")
    sum_c, avg_c = calculate_and_update_average_score_ratings(
        column_c, "Work-Life Balance")
    scores_worksheet = SHEET.worksheet("employee_survey_data")
    scores_worksheet.append_row([avg_a, avg_b, avg_c])

    print(f"Employee Satisfaction - Sum: {sum_a}, Average: {avg_a}")
    print(f"Job Satisfaction - Sum: {sum_b}, Average: {avg_b}")
    print(f"Work-Life Balance - Sum: {sum_c}, Average: {avg_c}")


print("Welcome to project_employee_ratings Data Automation")
main()
