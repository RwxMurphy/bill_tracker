import os
import shutil
from bills_logo import bills_logo

def welcome_screen():
    # get the size of the terminal window
    term_col_size = shutil.get_terminal_size().columns
    logo = bills_logo

    # Welcome screen
    print(logo) 
    print(f'--------------- Sign In ---------------\n' )
    
# gets the users 
def get_user_sign_in():
    user_name: str = ''
    user_id: int = 0

    user_name = input('Enter your user name: ')
    user_id = int(input('Enter your user id: '))
    return user_name, user_id


# Menu selections
def select_option() -> int:
    user_name, user_id = get_user_sign_in() 
    user_option_selected: int = 0

    option_1: str = '\033[1m 1. View all you current bills.\033[0m'
    option_2: str = '\033[1m 2. Add a new bill.\033[0m'
    option_3: str = '\033[1m 3. Remove a bill.\033[0m'
    
    menu_options = f"""
*** Welcome {user_name}-{user_id} ***
Please enter the number that corresponds with the action you would like to take.\n
{option_1}
{option_2}
{option_3}
"""
    os.system('clear')
    print(menu_options)
    user_option_selected = int( input('What would you like to do: ') )
    return user_option_selected

if __name__ == '__main__':
    pass