from colorama import Fore
from validations import validate_inputs,validation_string
from users_csv import read_csv_users

def login_user():
    attempts = 0
    data = read_csv_users()
    while attempts != 3:
        user_name = validate_inputs(str, "Type your username: ", validation_string)
        password = validate_inputs(str, "Type your password: ", validation_string)
        for user in data:
            if user['username'] == user_name and user['password'] == password:
                return True

        attempts += 1
        print("User or password are wrong" if attempts <3 else "Many attemps, closing program...")
    
    return False