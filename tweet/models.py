from django.db import models
from twitteruser.models import TwitterUser
from django.urls import reverse, reverse_lazy

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(TwitterUser, related_name='tweets', on_delete=models.CASCADE)
    # user = models.ManyToManyField(TwitterUser, related_name='user_tweets')
    body = models.TextField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '@{} - {}'.format(str(self.user),str(self.created_on))

    def get_absolute_url(self):
        return reverse('tweet:tweet_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_on']



