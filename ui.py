import shutil
from bills_logo import bills_logo

# get the size of the terminal window
term_col_size = shutil.get_terminal_size().columns
logo = bills_logo

user_name: str = ''
user_id: int = 0

# Welcome screen
print(logo) 
print(f'--------------- Sign In ---------------\n' )
user_name = input('Enter your user name: ')
user_id = int(input('Enter your user id: '))


if __name__ == '__main__':
    print(f'\nuser name: {user_name} \nuser id: {user_id}')