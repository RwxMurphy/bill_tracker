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
    
    menu_options = f"""
--- Welcome {user_name} - {user_id} ---
please enter the number that corresponds with the action you would like to take.
1. View all you current bills.
2. Add a new bill.
3. Remove a bill
"""
    os.system('clear')
    print(menu_options)
    user_option_selected = input('What would you like to do: ')
    return user_option_selected

if __name__ == '__main__':
    pass