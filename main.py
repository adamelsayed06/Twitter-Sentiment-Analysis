from twitter_client import TwitterClient
from tweet_processor import TweetProcessor
import config
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return []

@app.route('/get_tweets')
def get_tweets():
    api = TwitterClient()
    tweet_processor = TweetProcessor()

    search = request.args.get('query')
    tweets = api.get_tweets(search)

    if not tweets:
        return jsonify #error message
    
    analyzed_tweets = [{}]
    positiveTweets = {}
    negativeTweets = {}

    for tweet in tweets:
        analyzed_tweets[tweet] = tweet_processor.get_tweet_sentiment(tweet)

    for analyzed_tweet in analyzed_tweets:
        if(analyzed_tweets[analyzed_tweet] > 0):
            positiveTweets.update({analyzed_tweet : 'positive'})
        else:
            negativeTweets.update({analyzed_tweet : 'negative'})

    response = {**positiveTweets, **negativeTweets}

    return jsonify(response)

@app.route('get_tweets_score')
def get_tweets_score():
    api = TwitterClient()
    tweet_processor = TweetProcessor()

    search = request.args.get('query')
    tweets = api.get_tweets(search)

    averageScore = 0

    for tweet in tweets:
        averageScore += tweet_processor.get_tweet_sentiment(tweet)
    averageScore *= 10

    return{ 'averageScore' : averageScore }


        
    




def main():
    api = TwitterClient() #creating an instance of the TwitterClient class
    tweet_processor = TweetProcessor() #creating an instance of the TweetProcessor class

    tweets = api.get_tweets("Donald Trump") #query "Donald Trump"


    if not tweets: #if no tweets are fetched
        print("No tweets found")
        return
    
    analyzed_tweets = [{}] #empty dictionary to store analyzed tweets
    for tweet in tweets:
        analyzed_tweets[tweet] = tweet_processor.get_tweet_sentiment(tweet)

    positiveTweets = []
    negativeTweets = []

    for tweet in analyzed_tweets:
        if analyzed_tweets[tweet] > 0: #sentiment value for tweet is positive
            positiveTweets.append(tweet)
        else:
            negativeTweets.append(tweet)

    print("Positive tweets percentage:" + len(positiveTweets)/len(tweets)*100)
    print("\n""Negative tweets percentage:" + len(negativeTweets)/len(tweets)*100)
    
    print("\n""Positive tweets:")
    for tweet in positiveTweets:
        print(tweet)

    print("\n""Negative tweets:")
    for tweet in negativeTweets:
        print(tweet)
