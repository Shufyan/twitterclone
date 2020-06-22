from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class ProfileView(LoginRequiredMixin, ListView):
    context_object_name = "tweets"
    model = Tweet
    template_name = "twitteruser/profile.html"

    def get(self, request, *args, **kwargs):
        context = {}
        curr_user_object = TwitterUser.objects.filter(pk=kwargs['pk'])
        curr_user_tweets = Tweet.objects.filter(user_id=kwargs['pk'])
        context['curr_user_object'] = curr_user_object
        context['curr_user_tweets'] = curr_user_tweets
        return render(request, self.template_name, context)


@login_required
def follow(request, pk):
    user = TwitterUser.objects.get(pk=pk)
    request.user.follows.add(user)

    return redirect('/' + str(user.pk) + '/')


@login_required
def unfollow(request, pk):
    user = TwitterUser.objects.get(pk=pk)
    # watch out, this should be .remove() instead of .delete()
    request.user.follows.remove(user)

    return redirect('/' + str(user.pk) + '/')


@login_required
def following(request):
    user = request.user
    # important to add .all() at the end!
    userprofiles = request.user.follows.select_related(None).all()

    return render(request, 'tweet/tweet_list.html', {'title': 'Following',
                                          'userprofiles': userprofiles})

@login_required
def followers(request):
    user = request.user
    # important to add .all() at the end!
    userprofiles = request.user.followed_by.select_related(None).all()

    return render(request, 'tweet/tweet_list.html', {'title': 'Followers',
                                          'userprofiles': userprofiles})

