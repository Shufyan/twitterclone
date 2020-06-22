from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tweet.models import Tweet
from django.contrib.auth.models import AbstractUser
from twitteruser.models import TwitterUser
from notification.models import Notification
from django.shortcuts import get_object_or_404
import re

# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class IndexView(LoginRequiredMixin, ListView):
    context_object_name = "tweets"
    model = Tweet
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        userprofiles_ids = []
        user = request.user
        userprofiles = request.user.follows.select_related(None).all()

        for each_user in userprofiles:
            userprofiles_ids.append(each_user.id)
        userprofiles_ids.append(user.id)

        tweet_objects = []
        tweet_objects = Tweet.objects.filter(user_id__in=userprofiles_ids).all().order_by('-created_on')
        return render(request, self.template_name, {'tweet_objects':tweet_objects})

class TweetListView(ListView):
    context_object_name = "tweets"
    model = Tweet
    template_name = "tweet/tweet_list.html"

    def get(self, request, *args, **kwargs):
        userprofiles_ids = []
        user = request.user
        userprofiles = request.user.follows.select_related(None).all()

        for each_user in userprofiles:
            userprofiles_ids.append(each_user.id)
        userprofiles_ids.append(user.id)

        tweet_objects = []
        tweet_objects = Tweet.objects.filter(user_id__in=userprofiles_ids).all().order_by('-created_on')
        return render(request, self.template_name, {'tweet_objects':tweet_objects})

class TweetDetailView(DetailView):
    context_object_name = "tweet_detail"
    model = Tweet
    # template_name = "tweet/tweet_detail.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        twitteruser_object = TwitterUser.objects.filter(pk=self.object.user_id)
        context['twitteruser_object'] = twitteruser_object
        return context


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    fields = ['body']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        body_text = self.object.body
        user_list = re.findall(r'@\w+', body_text)
        user_list_unique = list(set([item.lower() for item in user_list]))
        if user_list_unique:
            for each_user in user_list_unique:
                user_obj = TwitterUser.objects.get(username__iexact = each_user[1:].lower())
                if user_obj:
                    notification = Notification(user=user_obj, tweet=self.object)
                    notification.save()

        return super().form_valid(form)