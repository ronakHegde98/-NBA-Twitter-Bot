import tweepy
import players as players_file
import webscrapper as ws
import team 
import json


# keys provided by Twitter to access its API
CONSUMER_KEY = 'ldqrSZZG74pjM8eudw4lPpos1'
CONSUMER_SECRET = 'Nf8nVnVRymIVQDeILnU2Cgek17KS1dhdRJo0mhOHdFSAMy4osE'
ACCESS_KEY = '1075462996984508421-l1DYH7LjAMlnD4xZHIQcHLAsCpB6VE'
ACCESS_SECRET = 'fmTWwNL4D0Gux7PCHpMNUTeb2xIqT8TRawnjqS5VmcmKW'

# twitter requires all requests to use OAunth for authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# api class provides aprint(mention_tweet)ccess to the entire twitter RESTful API methods
api = tweepy.API(auth)

# list of mention tweets
mention_tweets = api.mentions_timeline()



mention_list = []


def livePlayerStats(playerName):
  pass


def liveTeamStats(teamName):
  pass
#
def checkPlayerStatus(mention_tweet):
  for x in range(len(players_file.playersList)):
    if(str(players_file.playersList[x]['firstName'] + players_file.playersList[x]['lastName']).upper() == mention_tweet):
      return True
  return False


def checkTeamStatus(mention_tweet):
  for index in range(len(team.teamList)):
    if(team.teamList[index].upper() == mention_tweet or mention_tweet in team.teamList[index].upper()):
      print("FOUND: " + mention_tweet + " in team list")
      return True
  return False

for x in range(len(mention_tweets)-1,0,-1):
  mention_tweet = str(mention_tweets[x].text.split(
      " ", 1)[1].strip().replace("#", ""))

  isPlayer = checkPlayerStatus(mention_tweet.replace("live","").strip().upper())

  if(isPlayer and "live" in mention_tweet):
    #livePlayerStats(mention_tweet.replace("live","").upper())
    pass
  elif(isPlayer):
    playerStats = ws.regularSeasonPlayer(mention_tweet.upper())

    api.update_status('@' + str(mention_tweets[x].user.screen_name) + '\n' + mention_tweet.lower() + ' 2018-2019 Stats:' + '\n\tAssists Per Game (APG): ' + str(playerStats[0]) + '\n\tPoints Per Game (PPG): ' + str(playerStats[1]) + '\n\tRebounds Per Game (RPG): ' + str(playerStats[2]))
  else:
    isTeam = checkTeamStatus(mention_tweet.replace("live", "").upper())

    if(isTeam and "live" in mention_tweet):
      #liveTeamStats(mention_tweet.replace("live",""))
      pass
    elif(isTeam):
      print(mention_tweet,end = " ")
      teamRecord = (ws.regularSeasonTeam(mention_tweet.upper()))
      streak_dict = ws.streakStatus(mention_tweet.upper())
      
      streak_string = " "
      for key in streak_dict:
        if(key == 'L'):
          api.update_status('@' + str(mention_tweets[x].user.screen_name) + '\n' + mention_tweet.lower() + ' 2018-2019 Record: ' + str(teamRecord[0]) + "-" + str(teamRecord[1]) + '\n' + 'Yikes! Currently on a ' + str(streak_dict[key])  + ' game(s) ' + key + 'osing streak')
        else:
          api.update_status('@' + str(mention_tweets[x].user.screen_name) + '\n' + mention_tweet.lower() + ' 2018-2019 Record: ' + str(teamRecord[0]) + "-" + str(teamRecord[1]) + '\n' + 'Yay! Currently on a ' + str(streak_dict[key])  + ' game(s) ' + key + 'inning streak')

    else:
      print("error! you are not a player or a team")



  


  