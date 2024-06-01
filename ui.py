import os
import shutil
import time
import random
from bills_logo import bills_logo

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
def get_user_sign_in():
    user_name: str = ''
    user_id: int = 0

    print(f'--------------- \033[3mSign In\033[0m ---------------\n')
    user_name = input('Enter your user name: ')
    user_id = int(input('Enter your user id: '))
    return user_name, user_id




# Menu selections
def select_option() -> int:
    user_name, user_id = get_user_sign_in() # sign-in called 
    user_option_selected: int = 0

    # call load screen before displaying the menu
    loader()

    option_1: str = '\033[1m 1. View current bills.\033[0m'
    option_2: str = '\033[1m 2. Add a new bill.\033[0m'
    option_3: str = '\033[1m 3. Remove a bill.\033[0m'
    
    menu_options = f"""
--- Welcome {user_name}-{user_id} ---\n
Please enter the number that corresponds with the action you would like to take.\n
{option_1}
{option_2}
{option_3}
"""
    #os.system('clear')
    print(menu_options)
    user_option_selected = int( input('What would you like to do: ') )
    return user_option_selected


    


if __name__ == '__main__':
    pass