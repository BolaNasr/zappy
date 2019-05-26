import sys
import csv
import requests 
#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
f_consumer_key=open("tweets_service/consumer_key.txt", "r")
consumer_key = f_consumer_key.read().strip()
f_consumer_key.close()

f_consumer_secret=open("tweets_service/consumer_secret.txt", "r")
consumer_secret = f_consumer_secret.read().strip()
f_consumer_secret.close()

f_access_key=open("tweets_service/access_key.txt", "r")
access_key = f_access_key.read().strip()
f_access_key.close()

f_access_secret=open("tweets_service/access_secret.txt", "r")
access_secret = f_access_secret.read().strip()
f_access_secret.close()



# defining the api-endpoint  
API_ENDPOINT = "http://web:8000/tweetsApi/"

def get_tweets(username):

    #http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #set count to however many tweets you want
    number_of_tweets = 100

    #get tweets
    tweets_for_csv = {}
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
        #create array of tweet information: username, tweet id, date/time, text
        tweets_for_csv["tweet%s"%tweet.id_str] =[username, tweet.id_str, tweet.created_at, tweet.text]

    # data to be sent to api 
    data = {'Tweets':tweets_for_csv}
    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = tweets_for_csv) 
    return r

