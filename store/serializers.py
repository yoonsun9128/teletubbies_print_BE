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
        fields = ("pk", "input_img", "output_img", "user")
        extra_kwargs = {
            "user": {"required": False}
        }
        

class OutputImageSerializer(serializers.ModelSerializer):#마이페이지에 아웃풋 이미지 가져오기 위한 시리얼라이즈
    class Meta:
        model = Image
        fields = ("output_img",)            

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.email
    class Meta:
        model = Comment
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Image
        fields = ("user", "output_img", "comment_set")

class ImageListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    filter = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    def get_filter(self, obj):
        return obj.filter.filter_name
    class Meta:
        model = Image
        fields = ("output_img","user", "filter", "id")