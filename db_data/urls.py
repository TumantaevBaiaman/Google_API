from django.contrib import admin
from django.urls import path, include
from .views import add_database


urlpatterns = [
    path('', add_database, name='home'),
]