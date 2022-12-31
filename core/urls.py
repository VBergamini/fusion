from django.urls import path
from .views import IndexView
from django.contrib import admin

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

