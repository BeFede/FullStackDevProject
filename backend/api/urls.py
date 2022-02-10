from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^cars/(?P<plate>.+)?/?$', views.CarView.as_view(), name='cars'),
]