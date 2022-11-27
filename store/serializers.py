from rest_framework import serializers
from store.models import Filter, Comment
from users.models import User
from ImageStorage.models import Image


class FilterSerializer(serializers.ModelSerializer): #Filter모델 시리얼라이즈
    class Meta:
        model = Filter
        fields = "__all__"

class ImageStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "input_img", "output_img")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Image
        fields = ("user", "output_img", "comment_set")
