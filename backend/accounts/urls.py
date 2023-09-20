"""URLs module for the accounts app."""
# pylint: disable=import-error
from django.urls import path
from .views import SignupView

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
]
