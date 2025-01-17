from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from store import serializers
from store.models import Filter, Comment
from users.models import User
from ImageStorage.views import style
from store.serializers import FilterSerializer, ImageStorageSerializer, ImageSerializer, CommentSerializer, ImageListSerializer, CommentPutSerializer
from ImageStorage.models import Image
import PIL


class StoreView(APIView):
    def get(self, request):
        filters = Filter.objects.all()
        serializer = FilterSerializer(filters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UploadImageView(APIView): # input 이미지만 넣는 페이지
    def get(self, request, filter_id):
        filter = Filter.objects.get(id=filter_id)
        serializer = FilterSerializer(filter)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
            style(slz_id, filter_name).save(uploadurl)
            outputimage.output_img = uploadurl[6:]
            outputimage.save()
            return Response(slz.data['output_img'], status=status.HTTP_200_OK)
        else:
            return Response(slz.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageView(APIView):
    def get(self, request):
        Images = Image.objects.all()
        serializer = ImageListSerializer(Images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, image_id):
        pass


class ImageDetailView(APIView):
    def get(self, request, image_id):
        image = Image.objects.get(id=image_id)
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, image_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, image_id=image_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #사진 자체를 삭제
    def delete(self, request, image_id):
        image = Image.objects.get(id=image_id)
        if request.user == image.user:
            image.delete()
        else:
            return Response("작성자가 아닙니다.",status=status.HTTP_406_NOT_ACCEPTABLE)

#댓글 수정 삭제
class CommentDetailView(APIView):
    def put(self, request, image_id, comment_id):
        comment = Comment.objects.get(id= comment_id)
        if request.user == comment.user:
            serializer = CommentPutSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, image_id, comment_id):
        comment = Comment.objects.get(id= comment_id)
        if request.user == comment.user:
            comment.delete()
        else:
            return Response("작성자가 아닙니다.",status=status.HTTP_406_NOT_ACCEPTABLE)

class ImageLikesView(APIView):
    def post(self, request, image_id):
        image = Image.objects.get(id=image_id)
        if request.user.is_anonymous:
            if request.user in image.likes.all():
                image.likes.remove(request.user)
                return Response("좋아요 취소되었습니다.", status=status.HTTP_202_ACCEPTED)
            else:
                image.likes.add(request.user)
                return Response("좋아요 추가되었습니다.", status=status.HTTP_202_ACCEPTED)
        else:
            return Response("로그인 해주세요.", status=status.HTTP_406_NOT_ACCEPTABLE)

