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
        

