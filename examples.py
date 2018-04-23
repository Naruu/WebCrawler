## twitter

from twitter import *

# Should fill in accessToken, accessTokenSecret, consumerKey, consumerSecret

t = Twitter(auth=OAuth(accessToken, accessTokenSecret, consumerKey,consumerSecret))
pythonTweets = t.search.tweets(q = "#python")
pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count = 5)
print(pythonTweets)

## check on https://twitter.com/search first

statusUpdate = t.statuses.update(status = 'Hello, world!')
print(statusUpdate)
