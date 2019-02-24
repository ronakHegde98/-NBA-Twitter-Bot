import tweepy
import players as players_file
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

def regularSeasonPlayer(playerName):
  pass

def regularSeasonTeam(teamName):
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
      



for x in range(len(mention_tweets)):
  mention_tweet = str(mention_tweets[x].text.split(
      " ", 1)[1].strip().replace("#", ""))

  isPlayer = checkPlayerStatus(mention_tweet.replace("live","").strip().upper())

  if(isPlayer and "live" in mention_tweet):
    livePlayerStats(mention_tweet.replace("live","").upper())
  elif(isPlayer):
    regularSeasonPlayer(mention_tweet.upper())
  else:
    isTeam = checkTeamStatus(mention_tweet.replace("live", "").upper())
    if(isTeam and "live" in mention_tweet):
      liveTeamStats(mention_tweet.replace("live",""))
    elif(isTeam):
      regularSeasonTeam(mention_tweet)
    else:
      print("error! you are not a player or a team")



  


  





