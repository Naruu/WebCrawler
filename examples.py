## twitter

from twitter import *
import json
from pprint import pprint

# Should fill in accessToken, accessTokenSecret, consumerKey, consumerSecret

t = Twitter(auth=OAuth(accessToken, accessTokenSecret, consumerKey,consumerSecret))
pythonTweets = t.search.tweets(q = "#python")
pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count = 5)
pprint(pythonTweets)

## check on https://twitter.com/search first

statusUpdate = t.statuses.update(status = 'Hello, world!')
pprint(statusUpdate)

world_trends = twitter.trends.available(_woeid=1)
sfo_trends = twitter.trends.place(_id = 2487956)
pprint(json.dumps(sfo_trends, indent=4)))



