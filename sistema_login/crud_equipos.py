from validations import validate_inputs, validation_string

def create_team(teams_list ,team_name, city, league):
    if team_exist(teams_list, team_name):
        print("The team already exists")
    else:
        team = {
            'name' : team_name,
            'city' : city,
            'league' : league
        }
        teams_list.append(team)
        print(f"The team {team['name']} has been added")
    return teams_list

def list_teams(teams_list):
    print(f"{'Team name':<15}|{'City':<10}|{'League':<10}")
    print(teams_list)
    for team in teams_list:
        print(f"{team['name']:<15}|{team['city']:<10}|{team['league']:<10}".title())


def team_exist(teams_list, team_name):
    result = list(filter(lambda x : x['name'] == team_name, teams_list))
    return result

def update_team(team, key ,value):
    team[0][key] = value
    return print(f"Team updated {key} changed to {value}")

def update_team_menu(teams_list, team_name):
    if team_exist(teams_list, team_name):
        team = team_exist(teams_list, team_name)
        while True:
            print("=====Choose, what do you update?====")
            print("1. Update name")
            print("2. Update city")
            print("3. Update league")
            print("0. Back")
            opcion = validate_inputs(str, "Choose an option: ", validation_string)
            match opcion:
                case '1':
                    value_update = validate_inputs(str, "Type the new name for team: ")
                    update_team(team, "name",value_update)
                case '2':
                    value_update = validate_inputs(str, "Type the new city for team: ")
                    update_team(team, "city",value_update)
                case '3':
                    value_update = validate_inputs(str, "Type the new league for team: ")
                    update_team(team, "league",value_update)
                case '0':
                    break
                case _ :
                    print("Invalid option")
    else:
        print("Team does not exist")

def delete_team(teams_list, team_name):
    if team_exist(teams_list, team_name):
        team_to_remove = team_exist(teams_list, team_name)
        teams_list.remove(team_to_remove[0])
        return print(f"Team {team_to_remove[0]['name']} has been eliminated")
    else:
        print("Team does not exist")

