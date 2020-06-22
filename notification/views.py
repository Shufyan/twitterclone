from django.shortcuts import render
from .models import Notification
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from tweet.models import Tweet
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

# Create your views here.
class NotificationListView(LoginRequiredMixin, ListView):
    context_object_name = "notifications"
    model = Notification
    template_name = "notification/notification_list.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        user_notifications = user.user_notifications.all()

        tweet_objects = []
        for each_not in user_notifications:
            tweet_objects.append(Tweet.objects.get(pk=each_not.tweet_id))
            each_not.delete()

        return render(request, self.template_name, {'notification_count':user_notifications.count(),'tweet_objects':tweet_objects})