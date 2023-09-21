# pylint: disable=import-error
"""Realtors views"""
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Realtor
from .serializers import RealtorSerializer


# Create your views here.
class RealtorListView(ListAPIView):
    """Realtor list view"""
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None


class RealtorView(RetrieveAPIView):
    """Realtor view"""
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    permission_classes = (permissions.AllowAny,)


class TopSellerView(ListAPIView):
    """Top seller view"""
    queryset = Realtor.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
