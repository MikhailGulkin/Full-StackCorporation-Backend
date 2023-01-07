from project.models import Team


def create_team(team_number, start=1):
    return [
        Team.objects.create(
            team_name=f'team_{index}'
        ) for index in range(start, team_number)
    ]
