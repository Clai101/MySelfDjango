
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from .views import MainListView

urlpatterns = [
    path('', MainListView.as_view(), name='main'),
    ]