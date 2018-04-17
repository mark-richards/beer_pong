from .models import Match, Season, Team

# teams = ["Richo", "Pmac", "Matt", "Kappaz", "Garter", "Melons", "Lester", "Chief", "Melbourne", "Cats", "Dons", "Tigers", "GWS", "BEEECCCC"]
# teams = ["Richo", "Pmac", "Matt", "Kappaz", "Bec", "Kram", "Lester", "Garter"]
# teams = [
#     "Test1",
#     "Test2",
#     "Test3",
#     "Test4",
#     "Test5",
#     "Test6",
#     "Test7",
#     "Test8",
#     "Test9",
#     "Test10",
#     "Test11",
#     "Test12",
#     "Test13",
#     "Test14"
# ]




def get_round_one(number_of_teams, fixture_list):
    for index in range(int(number_of_teams / 2)):
        round_number = 1
        home_team = index + 1
        away_team = number_of_teams - index
        if home_team == away_team:
            exit()
        fixture_list.append({
            "round": round_number,
            "home_team": home_team,
            "away_team": away_team
        })


def get_remaining_rounds(number_of_teams, fixture_list):
    for round_number in range(2, number_of_teams):
        previous_round_start = len(fixture_list) - int(number_of_teams / 2)
        for index in range(int(number_of_teams / 2)):
            previous_round_home = fixture_list[index + previous_round_start]["home_team"]
            previous_round_away = fixture_list[index + previous_round_start]["away_team"]

            a = previous_round_home + number_of_teams / 2
            if a > number_of_teams - 1:
                current_round_home = previous_round_home - (number_of_teams / 2 - 1)
            else:
                current_round_home = a

            b = previous_round_away + number_of_teams / 2
            if b > number_of_teams - 1:
                current_round_away = previous_round_away - (number_of_teams / 2 - 1)
            else:
                current_round_away = b

            if previous_round_home == number_of_teams:
                current_round_away = number_of_teams
                c = previous_round_away + number_of_teams / 2
                if c > number_of_teams - 1:
                    current_round_home = previous_round_away - (number_of_teams / 2 - 1)
                else:
                    current_round_home = c

            if previous_round_away == number_of_teams:
                current_round_home = number_of_teams
                d = previous_round_home + number_of_teams / 2
                if d > number_of_teams - 1:
                    current_round_away = previous_round_home - (number_of_teams / 2 - 1)
                else:
                    current_round_away = d

            fixture_list.append({
                "round": round_number,
                "home_team": current_round_home,
                "away_team": current_round_away
            })


def generate_season(season, teams):
    number_of_teams = len(teams)
    fixture_list = []

    get_round_one(number_of_teams, fixture_list)
    get_remaining_rounds(number_of_teams, fixture_list)

    season = Season(name=season)
    season.save()

    for fixture in fixture_list:
        home_team, created = Team.objects.get_or_create(name=teams[int(fixture["home_team"])-1])
        home_team.save()
        
        away_team, created = Team.objects.get_or_create(name=teams[int(fixture["away_team"])-1])
        away_team.save()

        match = Match(
            season=season,
            round=fixture["round"],
            home_team=home_team,
            away_team=away_team
        )

        match.save()
    return season.id
