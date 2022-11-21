from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from store import serializers
from store.models import Filter, Filter_option, Filter_size, Review
from store.serializers import FilterSerializer, FilterSizeOptionSerializer
from django.db.models.query_utils import Q
# Create your views here.
class StoreView(APIView):
    def get(self, request):
        filters = Filter.objects.all()
        serializer = FilterSerializer(filters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class OptionSettingPageView(APIView):
    def get(self, request, filter_id):
        filter_option = get_object_or_404(Filter_option, id=filter_id)
        serializer = FilterSizeOptionSerializer(filter_option, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, filter_id):
        리뷰
        pass

    
class OrderPageView(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass