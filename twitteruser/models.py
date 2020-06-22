from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TwitterUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    follows = models.ManyToManyField('self',related_name='followed_by',symmetrical=False)

    def __str__(self):
        return "{}".format(self.username)


# AbstractUser.twitteruser = property(lambda u: TwitterUser.objects.get_or_create(username=u)[0])