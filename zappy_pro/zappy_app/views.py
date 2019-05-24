from django.shortcuts import render
import requests

from django.http import HttpResponse

from .models import Tweets


def home(request):

    all_Tweets =  Tweets.objects.all()
    tweets_response=[]
    for tweet in all_Tweets:
        tweets_response.append(tweet.tweet_text)
    return HttpResponse(tweets_response)


def Api(request):

    data = request.POST
    for tweet in data.lists():
        tweet_field = Tweets(tweet_id=tweet[1][1],created_at=tweet[1][2],tweet_text=tweet[1][3],user_name=tweet[1][0])
        tweet_field.save()
    return HttpResponse("successfully")
# Create your views here.
