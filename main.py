import ui
from loader import loader

ui.welcome_screen() # Prints out logo
user_name, user_id, new_user = ui.sign_in_user() # sign-in user
loader() # calls the load screen 
user_choice: int = ui.select_option(user_name, user_id,) # prints menu and gets user choice

'''Display view based on the user selected_option'''
while user_choice != 0:
    if user_choice == 1:
        ui.current_bills_view(new_user)
    elif user_choice == 2:
        ui.add_bill_view(new_user)
    elif user_choice == 3:
        ui.remove_bill_view(new_user)
    user_choice: int = ui.select_option(user_name, user_id) # prints menu and gets user choice

ui.sign_out(new_user)


if __name__ == '__main__':
    pass
