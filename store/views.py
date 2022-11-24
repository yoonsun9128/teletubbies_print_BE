from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from store import serializers
from store.models import Filter, Filter_option, Review
from users.models import User
from ImageStorage.views import style
from store.serializers import FilterSerializer, FilterSizeOptionSerializer, ReviewSerializer, ReviewCreateSerializer, OrderPageSerializer, OrderCreateSerializer, ImageStorageSerializer
from django.db.models.query_utils import Q
from ImageStorage.models import Image
import PIL

class StoreView(APIView):
    def get(self, request):
        filters = Filter.objects.all()
        serializer = FilterSerializer(filters)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OptionSettingPageView(APIView):
    def get(self, request, filter_id):
        filter = get_object_or_404(Filter, id=filter_id)
        filter_option = filter_option.filter
        reviews = filter.review_set.all()
        serializer = OptionReviewSerializer(filter)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, filter_id):
        data = request.data
        filter = Filter.objects.get(id=filter_id)
        filter_name = filter.filter_image
        slz = ImageStorageSerializer(data=data)
        if slz.is_valid():
            slz.save(user=request.user)
            slz_id = slz.data['pk']
            number = slz_id
            uploadurl = f'media/output/save{number}.jpg'
            output_img = style(slz.data['input_img'], filter_name).save(uploadurl)
            outputimage = Image.objects.get(pk=slz_id)
            outputimage.output_img = uploadurl
            outputimage.save()
            return Response(slz.data['output_img'], status=status.HTTP_200_OK)    
        else:
            return Response(slz.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ReviewView(APIView):
    def get(self, request, filter_id):
        filter = Filter.objects.get(id=filter_id)
        reviews = filter.review_set.all()
        serializer = ReviewSerializer(reviews)
        return Response(serializer.data, status=status.HTTP_200_OK)



        
class OrderPageView(APIView):
    def get(self, request, filter_id):
        filter = Filter.objects.get(id=filter_id)
        serializers = OrderPageSerializer(filter)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request, user_id):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, user_id=user_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


              