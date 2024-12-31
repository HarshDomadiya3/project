from django.urls import path
from . import views

urlpatterns = [
    path('latest-tweets/', views.get_latest_tweets, name='latest_tweets'),
]
