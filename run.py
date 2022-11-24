#Your code goes here
#You can delete these comments, but do not change the name of this file
#Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches_copy")


def get_sales_data():
    """
    Get sales figures input from the users
    """
    while True: #linhas 23 a 37 keep o código running
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        #Our get_sales_data function runs a while loop, that asks the user for data:
        data_str = input("Enter your data here: ")
        #It converts the string of data from the user into a list of values:
        sales_data = data_str.split(",")

        #And then we use a single if statement to call our validate data function, passing it our sales data list.
        #This functions check errors. If there is no errors, returns "true" (line 58), otherwise returns false (56)
        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data    
    
#create a new function to handle our validation:
def validate_data(values):
    """
    Inside the try, convert all strings values into integers.
    Raises ValueError of strings cannot be converted into Int,
    or if there arent exactly 6 values.
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

data = get_sales_data()