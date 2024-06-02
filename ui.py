import os
import shutil
import time
import random
from bills_logo import bills_logo
from user import User

# Transition screen
def loader(time_delay=0.1) -> None:
    term_width: int = shutil.get_terminal_size().columns
    os.system('clear')
    progress: list[str] = ['.']
    for i in range(0, random.randint(10,40)):
        progress.insert(1, '*')
        print(''.join(progress))
        time.sleep(time_delay)
        os.system('clear')



def welcome_screen():
    logo = bills_logo
    message: str = '\033[3mWelcome to...\033[0m'

    print('\n\n')
    print(message)
    print(logo)
    # add a 0.5s delay after printing the logo
    time.sleep(0.5)
    


# gets the users singn in info.
def sign_in_user() -> tuple:
    user_name: str = ''
    user_id: int = 0

    print(f'--------------- \033[3mSign In\033[0m ---------------\n')
    user_name = input('Enter your user name: ')
    user_id = int(input('Enter your user id: '))
    new_user = User(user_name, user_id)# create new_user object with user_name and user_id
    return user_name, user_id, new_user




# Menu selections
def select_option(user_name, user_id) -> int:
    user_option_selected: int = 0

    # call load screen before displaying the menu
    loader()

    option_1: str = '\033[1m 1. View current bills.\033[0m'
    option_2: str = '\033[1m 2. Add a new bill.\033[0m'
    option_3: str = '\033[1m 3. Remove a bill.\033[0m'
    option_4: str = '\033[1m 0. Exit.\033[0m'
    
    menu_options = f"""
--- {user_name}-{user_id} ---\n
Select an option from the menu.\n
{option_1}
{option_2}
{option_3}
{option_4}

"""
    #os.system('clear')
    print(menu_options)
    user_option_selected = int( input('Enter a number from the menu: ') )
    return user_option_selected


def current_bills_view(user: User) -> None:
    print(f'--- {user.name}-{user.user_id} current bills ---')
    list_of_bills: list[str] = user.list_all_bills()
    for bill in list_of_bills:
        print(f'- {bill}')
    
    print()
    input('Press ENTER to continue...')






def add_bill_view():
    pass

def remove_bill_view():
    pass

    


if __name__ == '__main__':
    pass