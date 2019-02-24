from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import Team
from basketball_reference_web_scraper import client


def regularSeasonPlayer(playerName):
    season19 = client.players_season_totals(season_end_year=2019)
    playerStats = []
    points = 0
    rebounds = 0

# for x in range(len(player_list)):
#    if(player_list[x]['team'] == Team.TORONTO_RAPTORS ):
#        print (player_list[x]['name'])

    # assists
    for x in range(len(season19)):
        if(season19[x]['name'].replace(" ", "").upper() == playerName):
            playerStats.append(
                round(((season19[x]['assists'])/(season19[x]['games_played'])), 1))
            # print((season19[x]['assists']))

    # points
    for x in range(len(season19)):
        if(season19[x]['name'].replace(" ", "").upper() == playerName):
            points = (points + (season19[x]['made_field_goals']-season19[x]['made_three_point_field_goals'])*2 + (
                season19[x]['made_three_point_field_goals'])*3 + (season19[x]['made_free_throws'])*1)/(season19[x]['games_played'])
            playerStats.append(round(points, 1))
            # print (points)

    # rebounds
    for x in range(len(season19)):
        if(season19[x]['name'].replace(" ", "").upper() == playerName):
            rebounds = (((season19[x]['offensive_rebounds'])) + (
                (season19[x]['defensive_rebounds'])))/(season19[x]['games_played'])
            playerStats.append(round(rebounds, 1))
            # print (rebounds)

    return playerStats


def regularSeasonTeam(teamName):

    seasonSchedule = client.season_schedule(season_end_year=2019)
    teamRecord = []
    wins = 0
    losses = 0

    for x in range(len(seasonSchedule)):
        if(seasonSchedule[x]['away_team_score'] == None):
            break
        else:
            if(str(seasonSchedule[x]['away_team']).replace("Team.", "").replace("_", "") == teamName or teamName in str(seasonSchedule[x]['away_team']).replace("Team.", "").replace("_", "")):
                if(seasonSchedule[x]['away_team_score'] > seasonSchedule[x]['home_team_score']):
                    wins += 1
                if(seasonSchedule[x]['away_team_score'] < seasonSchedule[x]['home_team_score']):
                    losses += 1
            if(str(seasonSchedule[x]['home_team']).replace("Team.", "").replace("_", "") == teamName or teamName in str(seasonSchedule[x]['home_team']).replace("Team.", "").replace("_", "")):
                if(seasonSchedule[x]['home_team_score'] > seasonSchedule[x]['away_team_score']):
                    wins += 1
                if(seasonSchedule[x]['home_team_score'] < seasonSchedule[x]['away_team_score']):
                    losses += 1


    teamRecord.append(wins)
    teamRecord.append(losses)
    return teamRecord



    
def streakStatus(teamName):
    seasonSchedule = client.season_schedule(season_end_year=2019)
    teamRecords = []

    for x in range(len(seasonSchedule)):
        if(seasonSchedule[x]['away_team_score'] == None):
            break
        else:
            if(str(seasonSchedule[x]['away_team']).replace("Team.", "").replace("_", "") == teamName or teamName in str(seasonSchedule[x]['away_team']).replace("Team.", "").replace("_", "")):
                teamRecords.append(seasonSchedule[x])
            elif(str(seasonSchedule[x]['home_team']).replace("Team.", "").replace("_", "") == teamName or teamName in str(seasonSchedule[x]['home_team']).replace("Team.", "").replace("_", "")):
                teamRecords.append(seasonSchedule[x])



    first_record = teamRecords[len(teamRecords)-1]

    if(str(first_record['away_team']).replace("Team.", "").replace("_", "") == teamName or teamName in str(first_record['away_team']).replace("Team.", "").replace("_", "")):
        print(first_record['away_team'])
        if(first_record['away_team_score'] > first_record['home_team_score']):
            lastGame = 'W'
        else:
            lastGame = 'L'
    else:
        if(first_record['home_team_score'] > first_record['away_team_score']):
            lastGame = 'W'
        else:
            lastGame = 'L'



    winningStreak = 0
    losingStreak = 0
    for index in range(len(teamRecords)-1, 0, -1):
        if(str(teamRecords[index]['away_team']).replace("Team.", "").replace("_", "") == teamName or teamName in str(teamRecords[index]['away_team']).replace("Team.", "").replace("_", "")):
            if(teamRecords[index]['away_team_score'] > teamRecords[index]['home_team_score']):
                if(lastGame == 'W'):
                    winningStreak += 1
                    continue
                else:
                    break
            else:
                if(lastGame == 'L'):
                    losingStreak += 1
                    continue
                else: 
                    break
        else:
            if(teamRecords[index]['home_team_score'] > teamRecords[index]['away_team_score']):
                if(lastGame == 'W'):
                    winningStreak += 1
                    continue
                else:
                    break
            else:
                if(lastGame == 'L'):
                    losingStreak += 1
                    continue
                else:
                    break

    if(lastGame == 'W'):
        return {'W':winningStreak}
    else:
        return {'L':losingStreak}


