from colorama import Fore
from validations import validate_inputs, validation_string
from login import login_user
from crud_equipos import create_team, list_teams

teams_list = []
def main_menu():
    if login_user():
        while True:
            print("==================MAIN MENU=================")
            print("1.Create team")
            print("2.list team")
            print("3.Upgrading an existing team")
            print("4.Delete team")
            print("0.Exit")
            opcion = validate_inputs(str, "Choose an option: ", validation_string)
            match opcion:
                case '1':
                    team_name = validate_inputs(str, "Type the name of team: ", validation_string).lower()
                    city = validate_inputs(str, "Type the team's city: ", validation_string).lower()
                    league = validate_inputs(str, "Type the team's league: ", validation_string).lower()
                    print(create_team(teams_list, team_name, city, league))
                case '2':
                    list_teams(teams_list)
                case '3':
                    print("3")
                case '4':
                    print("4")
                case '0':
                    break
                case _:
                    print(Fore.RED,"Invalid option", Fore.RESET)
    
