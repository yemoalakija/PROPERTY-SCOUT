# pylint: disable=import-error
"""Listings views"""
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer, ListingDetailSerializer
from datetime import datetime, timezone, timedelta


# Create your views here.
class ListingsView(ListAPIView):
    """Listings view"""
    queryset = Listing.objects.filter(is_published=True).order_by('-list_date')
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListingSerializer
    lookup_field = 'slug'


class ListingView(RetrieveAPIView):
    """Listing view"""
    queryset = Listing.objects.filter(is_published=True).order_by('-list_date')
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListingDetailSerializer
    lookup_field = 'slug'


class SearchView(APIView):
    """Search view"""
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListingSerializer

    def post(self, request, format=None):
        """Search view"""
        queryset = Listing.objects.filter(is_published=True).order_by('-list_date')
        data = self.request.data

        # Sale Type
        sale_type = data['sale_type']
        queryset = queryset.filter(sale_type__iexact=sale_type)

        # Home Type
        home_type = data['home_type']
        queryset = queryset.filter(home_type__iexact=home_type)

        # Price
        price = data['price']
        if price == '0+':
            price = 0
        elif price == '$100,000+':
            price = 100000
        elif price == '$200,000+':
            price = 200000
        elif price == '$300,000+':
            price = 300000
        elif price == '$400,000+':
            price = 400000
        elif price == '$500,000+':
            price = 500000
        elif price == '$600,000+':
            price = 600000
        elif price == '$700,000+':
            price = 700000
        elif price == '$800,000+':
            price = 800000
        elif price == 'Any':
            price = -1

        if price != -1:
            queryset = queryset.filter(price__gte=price)

        # Bedrooms
        bedrooms = data['bedrooms']
        if bedrooms == '0+':
            bedrooms = 0
        elif bedrooms == '1+':
            bedrooms = 1
        elif bedrooms == '2+':
            bedrooms = 2
        elif bedrooms == '3+':
            bedrooms = 3
        elif bedrooms == '4+':
            bedrooms = 4
        elif bedrooms == '5+':
            bedrooms = 5

        queryset = queryset.filter(bedrooms__gte=bedrooms)

        # Bathrooms
        bathrooms = data['bathrooms']
        if bathrooms == '0+':
            bathrooms = 0
        elif bathrooms == '1+':
            bathrooms = 1
        elif bathrooms == '2+':
            bathrooms = 2
        elif bathrooms == '3+':
            bathrooms = 3
        elif bathrooms == '4+':
            bathrooms = 4
        elif bathrooms == '5+':
            bathrooms = 5

        queryset = queryset.filter(bathrooms__gte=bathrooms)

        # Size in Square Feet(Sqft)
        sqft = data['sqft']
        if sqft == '1000+':
            sqft = 1000
        elif sqft == '1200+':
            sqft = 1200
        elif sqft == '1500+':
            sqft = 1500
        elif sqft == '2000+':
            sqft = 2000
        elif sqft == 'Any':
            sqft = -1

        if sqft != -1:
            queryset = queryset.filter(sqft__gte=sqft)

        # Days Listed
        days_listed = data['days_listed']
        if days_listed == '1 or less':
            days_listed = 1
        elif days_listed == '2 or less':
            days_listed = 2
        elif days_listed == '5 or less':
            days_listed = 5
        elif days_listed == '10 or less':
            days_listed = 10
        elif days_listed == '20 or less':
            days_listed = 20
        elif days_listed == 'Any':
            days_listed = -1

        if days_listed != -1:
            days_listed_date = datetime.today() - timedelta(days=days_listed)
            queryset = queryset.filter(list_date__gte=days_listed_date)

        # Has Photos
        has_photos = data['has_photos']
        if has_photos == '1+':
            has_photos = 1
        elif has_photos == '3+':
            has_photos = 3
        elif has_photos == '5+':
            has_photos = 5

        for query in queryset:
            count = 0
            if query.photo_1:
                count += 1
            if query.photo_2:
                count += 1
            if query.photo_3:
                count += 1
            if query.photo_4:
                count += 1
            if query.photo_5:
                count += 1
            if query.photo_6:
                count += 1
            if query.photo_7:
                count += 1
            if query.photo_8:
                count += 1
            if query.photo_9:
                count += 1
            if query.photo_10:
                count += 1

            if count < has_photos:
                slug = query.slug
                queryset = queryset.exclude(slug__iexact=slug)

        # Open House
        open_house = data['open_house']
        queryset = queryset.filter(open_house__iexact=open_house)

        # Keywords
        keywords = data['keywords']
        queryset = queryset.filter(description__icontains=keywords)

        serializer = ListingSerializer(queryset, many=True)

        return Response(serializer.data)
