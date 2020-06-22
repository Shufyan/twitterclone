from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(TwitterUser, related_name='user_notifications', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='tweet_notifications', on_delete=models.CASCADE)
    read_flag = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):        
        return "Notification id: {} - Tweet id: {} - User id: {}".format(str(self.pk), str(self.tweet), str(self.user))

