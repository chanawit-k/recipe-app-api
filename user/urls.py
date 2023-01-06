""" URL mapping for User api """
from django.urls import path

from user import views

app_name ='user'
urlpatterns = [
    path('create/', views.CreateUserview.as_view(), name='create'),
]