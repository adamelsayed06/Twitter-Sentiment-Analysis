from twitter_client import TwitterClient
from tweet_processor import TweetProcessor
import config
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return jsonify([])

@app.route('/get_tweets')
def get_tweets():
    api = TwitterClient()
    tweet_processor = TweetProcessor()

    search = request.args.get('query')
    tweets = api.get_tweets(search)

    if not tweets:
        return jsonify({"error": "no tweets found"}) #error message
    
    analyzed_tweets = {} #e.g. "I hate Donald Trump" : -0.78

    for tweet in tweets:
        analyzed_tweets[tweet["text"]] = tweet_processor.get_tweet_sentiment(tweet["text"]) #tweet is json object and we want the value of the 'text' key

    return jsonify(analyzed_tweets)

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

