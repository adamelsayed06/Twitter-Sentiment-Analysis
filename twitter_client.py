import tweepy #twitter api
from tweepy import OAuthHandler #authentication, b/c api is connected to my account

class TwitterClient():
    def __init__(self): #constructor class
        api_key = ""
        api_key_secret = ""

        access_token = ""
        access_secret = ""

        try:
            self.auth() = tweepy.OAuthHandler(api_key, api_key_secret) #authenticating with my account
            self.auth.set_access_token(access_token, access_secret) #make api calls on my behalf
            self.api = tweepy.API(self.auth) #create api instance

        except:
            print("Error: Authentication Failed")

    def get_tweets(self, query): #default count of tweets is 15, can be set as additional param
        tweets = [] #initalize the tweets we get fetch to an empty array

        try:
            fetched_tweets = self.api.search(query=query) #api requires explicit naming of parameters
            for fetched_tweet in fetched_tweets:
                tweets.append(fetched_tweet.text) #append text content/attribute of every fetched tweet to our array
            return tweets
        except tweepy.TweepyException as e:
            print(f"Error: {str(e)}")
            return tweets
        
    


