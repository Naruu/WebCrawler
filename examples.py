## twitter

from twitter import Twitter

t = Twitter(auth=OAuth(accessToken, accessTokenSecret, consumerKey,consumerSecret))
pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)
