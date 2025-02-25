import re #regex manipulation
from textblob import TextBlob #library for NLP which uses sentiment polarity to gauge if message is posiitive or negative

class TweetProcessor:
    #no instance attribute, so we dont need a constructor
    def clean_tweet(self, tweet):
        cleaned_text = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet) 
        #removing mentions, special character, and url with blank space from the tweet so sentiment analysis can work better
        return ' '.join(cleaned_text.split()) #returning the cleaned tweet broken down into words via single spacing

    def get_tweet_sentiment(self,tweet):
        analysis = TextBlob(self.clean_tweet(tweet)) #cleaning the tweet and passing it to TextBlob for Sentiment Analysis
        return analysis.sentiment.polarity
