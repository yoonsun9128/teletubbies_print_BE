from rest_framework import serializers
from store.models import Filter, Filter_option, Review
from users.models import User, Order
from ImageStorage.models import Image

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension







class FilterSerializer(serializers.ModelSerializer): #Filter모델 시리얼라이즈
    class Meta:
        model = Filter
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer): #구매옵션설정페이지 댓글부분 시리얼라이즈
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Review
        fields = ('review_image','content','user', 'updated_at', 'created_at')


class ReviewCreateSerializer(serializers.ModelSerializer): #구매옵션설정페이지 리뷰생성 시리얼라이즈
    class Meta:
        model = Review
        fields = ("content",)

class OrderCreateSerializer(serializers.ModelSerializer): #구매페이지 order생성 시리얼라이즈
    class Meta:
        model = Order
        fields = "__all__"


class ImageStorageSerializer(serializers.ModelSerializer): #인풋인미지와 아웃풋이미지 담는 시리얼라이즈
    input_img = serializers.FileField(required=False)
    class Meta:
        model = Image
        fields = ("pk", "input_img", "output_img")

class FilterOptionPriceSerializer(serializers.ModelSerializer): #filter_option에서 price만 가져오는 시리얼라이즈
    filter_set = FilterSerializer(many=True)
    class Meta:
        model = Filter_option
        fields = ("price",)

class FilterOptionSerializer(serializers.ModelSerializer): # filter_option에 대한 시리얼라이저
     class Meta:
        model = Filter_option
        fields = "__all__"

class OptionReviewSerializer(serializers.ModelSerializer): # 구매옵션설정페이지 옵션+리뷰 데이터 시리얼라이즈
    review_set = ReviewSerializer(many=True)
    filter_option_set = FilterOptionSerializer(many=True)
    class Meta:
        model = Filter
        fields = "__all__"

class FilterDetailUserSerializer(serializers.ModelSerializer):  #구매페이지에 user정보 넘기기 위한 시리얼라이즈
    class Meta:
        model = User
        fields = "__all__"

class FilterDetailImageSerializer(serializers.ModelSerializer):
    output_img = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model = Image
        fields = ("output_img",)

class FilterDetailPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter_option
        fields = "__all__"
class FilterDetailPageGetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)
        
class FilterDetailPageSerializer(serializers.ModelSerializer):
    user = FilterDetailPageGetUserSerializer(many=True)
    image = FilterDetailImageSerializer(many=True)
    filter_option = FilterDetailPriceSerializer(many=True)
    filter = FilterSerializer(many=True)
    class Meta:
        model = Order
        fields = "__all__"
        
class ReviewAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"



class FilterDetailPageGetSerializer(serializers.ModelSerializer):
    filter_user = FilterDetailUserSerializer(many=True)
    review_set = ReviewAllSerializer(many=True)
    image_set = FilterDetailImageSerializer(many=True)
    filter_option_set = FilterDetailPriceSerializer(many=True)
    class Meta:
        model = Filter
        fields = "__all__"