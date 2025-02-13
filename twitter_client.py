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


