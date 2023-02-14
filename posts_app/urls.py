from django.urls import path
from . import views

urlpatterns = [
    path('', views.Posts_list, name='post-list'),

]
