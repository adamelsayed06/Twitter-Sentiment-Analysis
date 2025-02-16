from twitter_client import TwitterClient
from tweet_processor import TweetProcessor
import config
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_tweets', methods = ['GET'])
def get_tweets():
    api = TwitterClient()
    tweet_processor = TweetProcessor()

    search = request.args.get('query')
    tweets = api.get_tweets(search)

    if not tweets:
        return jsonify({"error": "no tweets found"}) #error message
    
    analyzed_tweets = []
    #{text: I hate donald trump, score -0.9}
    #{text: I love donald trump, score 0.9}

    for tweet in tweets:
        analyzed_tweets.append(
            {
            "text": tweet["text"],
             "score": tweet_processor.get_tweet_sentiment(tweet["text"])
             })
         #tweet is json object and we want the value of the 'text' key

    return jsonify(analyzed_tweets)

@app.route('/get_tweets_score', methods = ['GET'])
def get_tweets_score():
    api = TwitterClient()
    tweet_processor = TweetProcessor()

    search = request.args.get('query')
    tweets = api.get_tweets(search)

    averageScore = 0

    for tweet in tweets:
        averageScore += tweet_processor.get_tweet_sentiment(tweet)
    averageScore /= len(tweets)
    averageScore *= 100

    return jsonify({'averageScore' : averageScore })

