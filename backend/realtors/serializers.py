# pylint: disable=import-error
"""Realtors views"""
from rest_framework import serializers
from .models import Realtor


# Create your serializers here.
class RealtorSerializer(serializers.ModelSerializer):
    """Realtor serializer"""
    class Meta:
        """Meta class"""
        model = Realtor
        fields = '__all__'
