# pylint: disable=import-error
from rest_framework import serializers
from .models import Contact


# Contact Serializer
class ContactSerializer(serializers.ModelSerializer):
    """Contact serializer"""
    class Meta:
        """Meta class"""
        model = Contact
        fields = '__all__'
