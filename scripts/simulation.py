#from scripts.team import get_team_rating
from scripts.team import get_team_roster
from scripts.team import get_team_id
from scripts.team import get_team_rating

teams = {
    "T1":"t1",
    "Gen.G":"geng"
}

def simulate_match(team1, team2, self):
    team1_id = get_team_id(team1)
    team2_id = get_team_id(team2)
    team1_rating = get_team_rating(team1)
    team2_rating = get_team_rating(team2)
    print(f"{team1} Rating: {team1_rating}")
    print(f"{team2} Rating: {team2_rating}")
    


    