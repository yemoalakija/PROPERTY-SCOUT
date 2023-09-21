# pylint: disable=import-error
"""Contacts admin"""
from django.urls import path
from .views import ContactView


# Create your views here.
urlpatterns = [
    path('', ContactView.as_view()),
]
