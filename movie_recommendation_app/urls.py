from django.contrib import admin
from django.urls import path
from movie_recommendation_app import views

urlpatterns = [
    path('', views.movie_recommendation, name='view')

]