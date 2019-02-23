import tweepy

#keys provided by Twitter to access its API 
CONSUMER_KEY = 'ldqrSZZG74pjM8eudw4lPpos1'
CONSUMER_SECRET = 'Nf8nVnVRymIVQDeILnU2Cgek17KS1dhdRJo0mhOHdFSAMy4osE'
ACCESS_KEY = '1075462996984508421-l1DYH7LjAMlnD4xZHIQcHLAsCpB6VE'
ACCESS_SECRET = 'fmTWwNL4D0Gux7PCHpMNUTeb2xIqT8TRawnjqS5VmcmKW'

#twitter requires all requests to use OAunth for authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#api class provides access to the entire twitter RESTful API methods 
api = tweepy.API(auth)

mention_tweets = api.mentions_timeline()
mention_list = []

for x in range(len(mention_tweets)):
    mention_tweet = mention_tweets[x].text.split(" ",1)[1].strip().replace("#","")
  

for x in range(len(mention_list)):
  print(mention_list[x])


'''ublic_tweets = api.home_timeline()
newString = public_tweets[0].text.upper().split(" ",1)[0].strip()

for x in range(len(public_tweets)):
  print(public_tweets[x].text + " " + str(public_tweets[x].id))
  '''