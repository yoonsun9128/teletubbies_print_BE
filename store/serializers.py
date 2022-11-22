from rest_framework import serializers
from store.models import Filter, Filter_option, Review
from users.models import User, Order

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
        fields = ('review_image','content','user', 'updated_at')
        

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
        
class OrderPageSerializer(serializers.ModelSerializer):
    user_set = OrderUserSerializer(many=True)
    class Meta:
        model = Filter_option
        fields = ("price", "reward", "username", "phone_number", "email", "address")