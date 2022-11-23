from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from store import serializers
from store.models import Filter, Filter_option, Review
from users.models import User
from store.serializers import FilterSerializer, FilterSizeOptionSerializer, ReviewSerializer, ReviewCreateSerializer, OrderPageSerializer, OrderCreateSerializer, OptionReviewSerializer
from django.db.models.query_utils import Q
# Create your views here.
class StoreView(APIView):
    def get(self, request):
        filters = Filter.objects.all()
        serializer = FilterSerializer(filters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OptionSettingPageView(APIView):
    def get(self, request, filter_id):
        filter = get_object_or_404(Filter, id=filter_id)
        serializer = FilterSizeOptionSerializer(filter, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class ReviewView(APIView):
    def get(self, request, filter_id):
        filter = Filter.objects.get(id=filter_id)
        reviews = filter.review_set.all()
        serializer = ReviewSerializer(reviews)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, filter_id):
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, filter_id=filter_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class OrderPageView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializers = OrderPageSerializer(user, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request, user_id):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, user_id=user_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class OptionReView(APIView):
    def get(self, request, filter_id):
        filter = get_object_or_404(Filter, id=filter_id)
        serializer = OptionReviewSerializer(filter)
        return Response(serializer.data, status=status.HTTP_200_OK)
              