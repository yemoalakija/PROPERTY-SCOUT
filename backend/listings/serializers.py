# pylint: disable=import-error
"""Listings serializers"""
from rest_framework import serializers
from .models import Listing


# Listing serializer
class ListingSerializer(serializers.ModelSerializer):
    """Listing serializer"""

    class Meta:
        """Meta class"""
        model = Listing
        fields = ('title', 'address', 'city', 'state', 'zipcode', 'description', 'sale_type', 'home_type', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size', 'photo_main', 'slug')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ListingDetailSerializer(serializers.ModelSerializer):
    """Listing detail serializer"""

    class Meta:
        """Meta class"""
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
