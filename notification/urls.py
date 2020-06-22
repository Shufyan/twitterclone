from django.conf.urls import url
from notification import views

app_name = "notification"

urlpatterns = [        
    url(r'^notifications/$', views.NotificationListView.as_view(), name='notifications'),   
]