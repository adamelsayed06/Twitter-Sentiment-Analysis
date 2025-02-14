from twitter_client import TwitterClient
from tweet_processor import TweetProcessor

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