from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('data_update/', views.data_update.as_view(), name='register'),

]

