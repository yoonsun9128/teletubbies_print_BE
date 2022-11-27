from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from store import serializers
from store.models import Filter, Review
from users.models import User
from ImageStorage.views import style
from store.serializers import FilterSerializer, ReviewSerializer, ImageStorageSerializer, FilterDetailPageSerializer,FilterDetailPageGetSerializer
from ImageStorage.models import Image
import PIL

class StoreView(APIView):
    def get(self, request):
        filters = Filter.objects.all()
        serializer = FilterSerializer(filters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UploadImageView(APIView): # input 이미지만 넣는 페이지
    def post(self, request, filter_id):
        data = request.data
        filter = Filter.objects.get(id=filter_id)
        filter_name = filter.filter_image
        slz = ImageStorageSerializer(data=data)
        if slz.is_valid():
            outputimage = slz.save(user=request.user, filter_id=filter_id)
            slz_id = slz.data['pk']
            number = slz_id
            uploadurl = f'media/output/save{number}.jpg'
            style(slz.data['input_img'], filter_name).save(uploadurl)
            outputimage.output_img = uploadurl
            outputimage.save()
            return Response(slz.data['output_img'], status=status.HTTP_200_OK)
        else:
            return Response(slz.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class ArticleView(APIView):
    def get(self, request, image_id):
        pass
    def post(self, request, image_id):
        pass
        
        
class ArticleDetailView(APIView): 
    def get(self, request, filter_id):
        filter = Filter.objects.get(id=filter_id)
        serializer = FilterDetailPageGetSerializer(filter, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, filter_id):
        serializer = FilterDetailPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

