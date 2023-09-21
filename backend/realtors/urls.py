# pylint: disable=import-error
"""Realtors views"""
from django.urls import path
from .views import RealtorListView, RealtorView, TopSellerView

# Create your views here.
urlpatterns = [
    path('', RealtorListView.as_view()),
    path('<int:pk>', RealtorView.as_view()),
    path('topseller', TopSellerView.as_view()),
]
