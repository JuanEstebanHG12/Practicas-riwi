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
    for team in teams_list:
        print(f"{team['name']:<15}|{team['city']:<10}|{team['league']:<10}".title())


def team_exist(teams_list, team_name):
    result = list(filter(lambda x : x['name'] == team_name, teams_list))
    return bool(result)