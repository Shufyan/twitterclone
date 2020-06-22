from django.conf.urls import url
from tweet import views

app_name = "tweet"

urlpatterns = [        
    url(r'^compose/$', views.TweetCreateView.as_view(), name='tweet_create'),     
    url(r'^tweet/(?P<pk>\d+)/$', views.TweetDetailView.as_view(), name="tweet_detail"),   
]