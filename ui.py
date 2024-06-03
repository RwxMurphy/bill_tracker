import os
import shutil
import time
import random
from bills_logo import bills_logo
from user import User
from loader import loader

# Transition screen
# def loader(time_delay=0.1) -> None:
#     term_width: int = shutil.get_terminal_size().columns
#     os.system('clear')
#     progress: list[str] = ['*']
#     for i in range(0, random.randint(10, 20)):
#         progress.insert(1, '*')
#         print(''.join(progress))
#         time.sleep(time_delay)
#         os.system('clear')



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
    os.system('clear')
    user_option_selected: int = 0
    # set menu options
    option_1: str = '\033[1m 1. View current bills.\033[0m'
    option_2: str = '\033[1m 2. Add a new bill.\033[0m'
    option_3: str = '\033[1m 3. Remove a bill.\033[0m'
    option_4: str = '\033[1m 0. Exit.\033[0m'
    
    menu_options = f"""
--- {user_name}-{user_id} ---
_____________________________
Select an option from the menu.
_____________________________
{option_1}
{option_2}
{option_3}
{option_4}
"""
    #os.system('clear')
    print(menu_options)
    user_option_selected = int( input('\nEnter a number from the menu: ') )
    print()
    return user_option_selected






def current_bills_view(user: User) -> None:
    os.system('clear')
    print(f'--- {user.name}-{user.user_id} current bills ---\n_________________________')
    list_of_bills: list[str] = user.list_all_bills()
    for bill in list_of_bills:
        print(f'- {bill}')
    
    print()
    input('Press ENTER to continue...')






def add_bill_view(user:User):
    os.system('clear')
    date_format:str = '\033[1m yyyy,m,d\033[0m'
    date_instruct:str = f'''
Enter the date in the following format:
{date_format} 
Example June 25th 2024 would be: 
2024,6,25
Do not use leading zeros \nExample 06 should be entered as 6.
'''
    print(f'--- Creating New Bill ---\n_________________________')
    name: str = input('\nWhat is the name of the bill?\n')
    amount: float = float( input(f'\nWhat is the amount due for your {name} bill?\n $') )
    
    os.system('clear')
    print(date_instruct)
    due_date = input(f'\nPlease enter the due date for your {name} bill in the format {date_format}.\n')

    # call the add_new_bill method on the user
    user.add_new_bill(name, amount, due_date)

    os.system('clear')
    print(f"\nYour '{name}' bill was added to your expenses.")
    input('\nPress ENTER to continue...')




def remove_bill_view(user: User):
    os.system('clear')
    print(f'--- Remove Bill ---\n_________________________')
    print(f'Here are all your current bills \n_________________________')
    bills_list = user.list_all_bills()
    for bill in bills_list:
        print(f'- {bill}')
    
    name: str = input('\nEnter the name of the bill you want to remove:\n')
    print(f'\nAre you sure you want to remove {name}?')
    warning: str = input(f"Enter 'n' (no) or 'y' (yes)\n")
    if warning == 'y':
        user.remove_bill(name)
        print(f'{name} bill was REMOVED!\n')
    else:
        print(f'{name} was NOT removed and is still being tracked\n')

    
    input('\nPress ENTER to continue...\n')
    





def sign_out(user: User) -> None:
    os.system('clear')
    print('Thank You For Using Bills....')
    print(f'\n{user.name}-{user.user_id} signed-out!')
    print('_____________________________\n')




    


if __name__ == '__main__':
    pass