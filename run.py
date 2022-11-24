# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    #print(f"The data provided is {data_str}")
    """
    Use input() method to get sales data  from the user in the terminal
    """

    sales_data = data_str.split(",") #split() method returns the broken up values as a lsit
    validate_data(sales_data) 

#create a new function to handle our validation:
def validate_data(values):
    """
    Inside the try, convert all strings values into integers.
    Raises ValueError of strings cannot be converted into Int,
    or if there arent exactly 6 values.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

get_sales_data() 
#RESULTADO: os values tem q estar numa lista:
#Enter your data here: 1,2,3,4,5,6,5
#['1', '2', '3', '4', '5', '6', '5']