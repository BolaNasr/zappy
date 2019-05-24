from django.db import models

class Tweets(models.Model):
    tweet_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=False, auto_now=False)
    tweet_text = models.CharField(max_length=30, null=True)
    user_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.tweet_text
# Create your models here.
