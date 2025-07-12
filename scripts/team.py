import json

team_ids = {
    "T1":"t1",
    "Gen.G":"geng"
}

role_ids = {
    "Top Laner": 0,
    "Jungler": 1,
    "Mid Laner": 2,
    "Bot Laner": 3,
    "Support": 4
}

def get_team_roster(team): #pass in team, not ID
    team_id = team_ids[team]
    roster = []
    with open('data/teams.json', 'r') as f:
        teams = json.load(f)
    for team in teams:

        if team["team_id"] == team_id:
            for player in team["team_players"]:
                roster.append(f"{player["name"]} - {player["overall"]} OVR")
    return roster

def get_team_id(team):
    return team_ids[team]

def get_role_id(player_role):
    return role_ids[player_role]

def get_team_rating(raw_team):
    weights = [0.2,0.2,0.2,0.2,0.2]
    team_id = get_team_id(raw_team)
    rating = 0

    with open('data/teams.json', 'r') as f:
        teams = json.load(f)
    for team in teams:
        if team["team_id"] == team_id:
            for player in team["team_players"]:
                player_role_id = get_role_id(player["role"])
                rating += player["overall"] * weights[player_role_id]
    return round(rating, 2)
