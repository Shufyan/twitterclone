from django.urls import path
from django.conf.urls import url

from . import views 

app_name = "accounts"

urlpatterns = [    
    url(r'^(?P<pk>\d+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^(?P<pk>\d+)/follow$', views.follow, name='follow'),
    url(r'^(?P<pk>\d+)/unfollow$', views.unfollow, name='unfollow'),
    url(r'^following/$', views.following, name='following'),
    url(r'^followers/$', views.followers, name='followers'),
]