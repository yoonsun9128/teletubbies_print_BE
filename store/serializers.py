from rest_framework import serializers
from store.models import Filter, Filter_option, Review
from users.models import User, Order
from ImageStorage.models import Image
class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Review
        fields = ('review_image','content','user', 'updated_at', 'created_at')
        

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("content",)
    

class FilterSizeOptionSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)
    class Meta:
        model = Filter_option
        fields = "__all__"
                

class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ("username", "phone_number", "email", "address", "reward")
        
class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        
class ImageStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

class FilterOptionPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter_option
        fields = ("price",)
        
class OrderPageSerializer(serializers.ModelSerializer): #구매페이지, 주문자정보(user이름, 번호, 이메일, 주소, 적립금 // 상품금액)
    image_set = ImageStorageSerializer(many=True)
    price_set = FilterOptionPriceSerializer(many=True)
    class Meta:
        model = User
        fields = ("username", "phone_number", "email", "address", "reward")

class FilterOptionSerializer(serializers.ModelSerializer): # filter_option에 대한 시리얼라이저
     class Meta:
        model = Filter_option
        fields = "__all__"

class OptionReviewSerializer(serializers.ModelSerializer): # 오더와 리뷰를 합친 serializer
    review_set = ReviewSerializer(many=True)
    filter_option_set = FilterOptionSerializer(many=True)
    class Meta:
        model = Filter
        fields = "__all__"
    

