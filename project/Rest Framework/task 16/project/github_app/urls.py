from django.urls import path
from . import views

urlpatterns = [
    path('list-repos/', views.list_repos, name='list_repos'),
    path('create-repo/', views.create_repo, name='create_repo'),
]
