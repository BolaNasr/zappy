import sys
import csv
import requests 
#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
#bad solution 
consumer_key = "sKPZPpCbbWNUak2NgYkcSDpfy"
consumer_secret = "wpW6Ve16upB2mfNwnMW4pykCnpSLkx2dISu4Pq4MkAWP1kmXkw"
access_key = "1103596494861553664-jHN1xiE9LvIDDJ0nDCy7nl7mrJsUZB"
access_secret = "esKxnoCi8CLPjLE0ydlJdHv85x2rrmb2uCuGDixrPWYWt"
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

