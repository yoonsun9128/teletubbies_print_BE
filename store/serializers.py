from rest_framework import serializers
from store.models import Filter, Filter_option, Review

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = "__all__"
        

class FilterSizeOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter_option
        fields = "__all__"
        

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Review
        fields = ('review_image','content','user',)
        
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("content",)
        