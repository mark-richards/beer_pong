from .models import Match, Team
import pprint


def get_team_dict(team_name):
    return {
        'team': team_name,
        'played': 0,
        'wins': 0,
        'losses': 0,
        'draws': 0,
        'points': 0,
        'cup_diff':0
    }


def get_ladder_data(season_id):
    matches = Match.objects.filter(season=season_id)
    data = {}

    for match in matches:
        if match.home_team.name not in data:
            data[match.home_team.name] = get_team_dict(match.home_team.name)
        if match.away_team.name not in data:
            data[match.away_team.name] = get_team_dict(match.away_team.name)

        if match.home_cups_remaining is None:
            pass

        elif match.home_cups_remaining < match.away_cups_remaining:
            data[match.home_team.name]['played'] += 1
            data[match.home_team.name]['wins'] += 1
            data[match.away_team.name]['played'] += 1
            data[match.away_team.name]['losses'] += 1
            data[match.home_team.name]['cup_diff'] += match.away_cups_remaining
            data[match.away_team.name]['cup_diff'] -= match.away_cups_remaining

        elif match.home_cups_remaining > match.away_cups_remaining:
            data[match.away_team.name]['played'] += 1
            data[match.away_team.name]['wins'] += 1
            data[match.home_team.name]['played'] += 1
            data[match.home_team.name]['losses'] += 1
            data[match.home_team.name]['cup_diff'] -= match.home_cups_remaining
            data[match.away_team.name]['cup_diff'] += match.home_cups_remaining

    results = list(data.values())
    results.sort(key=lambda i: (i['wins'],i['cup_diff']), reverse=True)
    pprint.pprint(results)
    return results


