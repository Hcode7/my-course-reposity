from django.urls import path
from . import views

urlpatterns = [
    path('sentiment', views.sentiment_analysis)
]