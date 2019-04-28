from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    date_created = models.DateTimeField(auto_now_add = True)
    content = models.CharField(max_length = 200, blank = True)
    tweet_id = models.UUIDField(primary_key = True,default = uuid4,editable = False)
    tweet_by = models.ForeignKey(User,on_delete = models.CASCADE)
    likes = models.IntegerField(default = 0)
    retweets = models.IntegerField(default = 0)
    attachment = models.ImageField(default ='default.png',blank = True)

    def __str__(self):
        return self.tweet_id
