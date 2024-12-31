from django.shortcuts import render

import tweepy
from django.conf import settings


def get_latest_tweets(request):
    
    api_key = settings.TWITTER_API_KEY
    api_secret_key = settings.TWITTER_API_SECRET_KEY
    access_token = settings.TWITTER_ACCESS_TOKEN
    access_token_secret = settings.TWITTER_ACCESS_TOKEN_SECRET

   
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = []
    username = request.GET.get('username')  

    if username:
        try:
            
            user_tweets = api.user_timeline(screen_name=username, count=5, tweet_mode='extended')
            tweets = [{'text': tweet.full_text, 'created_at': tweet.created_at} for tweet in user_tweets]
        except tweepy.TweepError as e:
            tweets = [{'error': str(e)}]

    return render(request, 'twitter_app/tweets.html', {'tweets': tweets})
